from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base, Category, Item, Transaction

# Connect to the database
engine = create_engine('sqlite:///farm_inventory.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Test query to check if tables exist
print("Categories:", session.query(Category).all())
print("Items:", session.query(Item).all())
print("Transactions:", session.query(Transaction).all())

session.close()