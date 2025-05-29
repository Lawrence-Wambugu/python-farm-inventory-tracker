from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Category, Item, Transaction
from datetime import datetime

# Connect to the database
engine = create_engine('sqlite:///farm_inventory.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Clear existing data to avoid duplicates
session.query(Transaction).delete()
session.query(Item).delete()
session.query(Category).delete()

# Seed Categories
categories = [
    Category(name="Crops"),
    Category(name="Livestock"),
    Category(name="Equipment")
]
session.add_all(categories)
session.commit()

# Seed Items
items = [
    Item(name="Maize", quantity=500.0, category_id=1),  # Crops
    Item(name="Wheat", quantity=300.0, category_id=1),  # Crops
    Item(name="Cows", quantity=20.0, category_id=2),    # Livestock
    Item(name="Goats", quantity=50.0, category_id=2),   # Livestock
    Item(name="Tractor", quantity=2.0, category_id=3),  # Equipment
    Item(name="Plow", quantity=5.0, category_id=3)      # Equipment
]
session.add_all(items)
session.commit()

# Seed Transactions
transactions = [
    Transaction(item_id=1, quantity=500.0, transaction_type="add", timestamp=datetime.utcnow()),  # Adding Maize
    Transaction(item_id=3, quantity=20.0, transaction_type="add", timestamp=datetime.utcnow()),   # Adding Cows
    Transaction(item_id=5, quantity=2.0, transaction_type="add", timestamp=datetime.utcnow())     # Adding Tractor
]
session.add_all(transactions)
session.commit()

print("Database seeded successfully!")
session.close()