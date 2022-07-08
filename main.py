from fastapi import FastAPI, Depends
import schemas
import models
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session 

Base.metadata.create_all(engine)

# separate session for each request so this function will be called for every request
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

app = FastAPI()

@app.get("/")
def getItems():
    return {"Message":"welcome to student database "}

@app.get("/items")
def getItems(session:Session=Depends(get_session)):
    items = session.query(models.Item).all()
    return items 

@app.get("/count")
def getItems(session:Session=Depends(get_session)):
    c=session.query(models.Item).count()  
    return c



@app.get("find/{id}")#path parameter 
def getItem(id:int, session: Session=Depends(get_session)):
    item = session.query(models.Item).get(id)
    return item



@app.post("/Add/{id}")
def addItem(item:schemas.Item, session:Session=Depends(get_session)):
    item = models.Item(Firstname = item.Firstname,Lastname = item.Lastname)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item 
   




@app.put("/{id}")
def updateItem(id:int, item:schemas.Item, session: Session= Depends(get_session)):
    itemObject = session.query(models.Item).get(id)
   
    itemObject.Firstname = item.Firstname
    itemObject.Lastname = item.Lastname
    session.commit()
    return itemObject


@app.delete("/{id}")
def deleteItem(id:int, session:Session= Depends(get_session)):
    itemObject = session.query(models.Item).get(id)
    session.delete(itemObject)
    session.commit()
    session.close()
    return {' deleted...{id} succesfully'}

