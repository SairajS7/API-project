#use to declare datatype 
from pydantic import BaseModel

#types
class Item(BaseModel):
    Firstname:str
    Lastname:str
   # task:str

    