from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
def add_Product(name, price, Picture_link, Description):

	Product_object = Product(
        name=name,
        price=price,
        Picture_link=Picture_link,
        Description=Description)
        session.add(Product_object)
        session.commit()



def Edit_product(Product_id, name):
   """
   Update a student in the database, with
   whether or not they have finished the lab
   """
   Product_object = session.query(
       Student).filter_by(
       Product_id=Product_id).first()
   Product_object.name = name
   session.commit()


def delete_Product(name):
   """
   Delete all students with a
   certain name from the database.
   """
   session.query(Student).filter_by(
       name=name).delete()
   session.commit()

def query_all():
   """
   Print all the students
   in the database.
   """
   products = session.query(
      Product).all()
   return products

def query_by_name(Product_id, name):
   """
   Find the first student
   in the database, by their name
   """
   product = session.query(
       name).filter_by(
       Product_id=Product_id).first()
   return product
   
def Add_to_Cart(ProductID):
	Cart_object = Product(ProductID = ProductID)
	session.add(Cart_object)
	session.commit()
