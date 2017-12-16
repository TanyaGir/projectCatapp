from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import datetime

Base = declarative_base()

class Category(Base):

    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name =  Column(String(250), nullable=False)

    @property
    def serialize(self):
           """Return object data in easily serializeable format"""
           return {
               'name'         : self.name,
               'id'           : self.id,
           }

class Item(Base):

    __tablename__ = 'item'

    item_name = Column(String(250), nullable=False)
    item_id = Column(Integer, primary_key=True)
    item_date = Column(DateTime, default=datetime.datetime.now)
    item_description = Column(String(250), nullable=False)
    cat_id = Column(Integer,ForeignKey('category.id'))

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'item_name'         : self.name,
           'id'                : self.id,
           'date'              : self.date,
           'description'       : self.description,
       }

engine = create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine)
