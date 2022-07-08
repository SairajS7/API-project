#use to create table in database 

from sqlalchemy import Column, Integer, String
from database import Base 

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    Firstname = Column(String(256))
    Lastname = Column(String(256))
    