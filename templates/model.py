from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
   __tablename__ = 'products'
   Product_id = Column(Integer, primary_key=True)
   name = Column(String)
   price = Column(Float)
   Picture_link = Column(String)
   Description = Column(String)

class cart(Base):
	__tablename__='ProductID'
	Product_id = Column(Integer, primary_key=True)




