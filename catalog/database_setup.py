from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

 
Base = declarative_base()
class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key = True)
    name =Column(String(250), nullable = False)
    email = Column(String(20), nullable=False)
    picture = Column(String(250))

class Category(Base):
    __tablename__ = 'category'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'id'           : self.id,
           'name'         : self.name
       }

    @property
    def serializeCategory(self):
       """Return object data in easily serializeable format"""
       return {
           'id'           : self.id,
           'name'         : self.name,
           'Title'         : self.name
       }
 
class CatalogItem(Base):
    __tablename__ = 'catalog_item'


    name =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    category_id = Column(Integer,ForeignKey('category.id'))
    category = relationship('Category',  primaryjoin="and_(CatalogItem.category_id==Category.id)",backref='catalog_item')
    user_id = Column(Integer,ForeignKey('user.id', onupdate="cascade"))
    user = relationship(User)


    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'description'         : self.description,
           'id'         : self.id
       }
	   
	   
    @property
    def serializeCatalogItem(self):
       """Return object data in easily serializeable format"""
       return {
           'cat_id'     : self.category_id,
           'description'         : self.description,
           'id'         : self.id,
           'name' : self.category.name,
           'Title'         : self.name
       }
       	   
engine = create_engine('sqlite:///categoryitems.db')
 

Base.metadata.create_all(engine)
