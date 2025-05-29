from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Category, Item, Transaction
from datetime import datetime

# Database setup
engine = create_engine('sqlite:///farm_inventory.db')
DBSession = sessionmaker(bind=engine)

def get_session():
    return DBSession()

def add_item(name, quantity, category_name):
    session = get_session()
    try:
        # Find or create category
        category = session.query(Category).filter_by(name=category_name).first()
        if not category:
            category = Category(name=category_name)
            session.add(category)
            session.commit()
        
        # Add item
        item = Item(name=name, quantity=quantity, category_id=category.id)
        session.add(item)
        session.commit()
        
        # Log transaction
        transaction = Transaction(item_id=item.id, quantity=quantity, transaction_type="add", timestamp=datetime.utcnow())
        session.add(transaction)
        session.commit()
        
        print(f"Added {quantity} {name} to {category_name}")
    except Exception as e:
        session.rollback()
        print(f"Error adding item: {e}")
    finally:
        session.close()

def view_inventory():
    session = get_session()
    try:
        items = session.query(Item, Category).join(Category).all()
        if not items:
            print("Inventory is empty.")
            return
        print("\nFarm Inventory:")
        print("ID | Name | Quantity | Category")
        print("-" * 40)
        for item, category in items:
            print(f"{item.id} | {item.name} | {item.quantity} | {category.name}")
    except Exception as e:
        print(f"Error viewing inventory: {e}")
    finally:
        session.close()

def update_item(item_id, name=None, quantity=None, category_name=None):
    session = get_session()
    try:
        item = session.query(Item).filter_by(id=item_id).first()
        if not item:
            print(f"Item with ID {item_id} not found.")
            return
        
        if name:
            item.name = name
        if quantity is not None:
            # Log transaction for quantity change
            if quantity != item.quantity:
                transaction = Transaction(
                    item_id=item.id,
                    quantity=quantity - item.quantity,
                    transaction_type="update",
                    timestamp=datetime.utcnow()
                )
                session.add(transaction)
            item.quantity = quantity
        if category_name:
            category = session.query(Category).filter_by(name=category_name).first()
            if not category:
                category = Category(name=category_name)
                session.add(category)
                session.commit()
            item.category_id = category.id
        
        session.commit()
        print(f"Item ID {item_id} updated.")
    except Exception as e:
        session.rollback()
        print(f"Error updating item: {e}")
    finally:
        session.close()

def delete_item(item_id):
    session = get_session()
    try:
        item = session.query(Item).filter_by(id=item_id).first()
        if not item:
            print(f"Item with ID {item_id} not found.")
            return
        # Log transaction
        transaction = Transaction(
            item_id=item.id,
            quantity=-item.quantity,
            transaction_type="delete",
            timestamp=datetime.utcnow()
        )
        session.add(transaction)
        session.delete(item)
        session.commit()
        print(f"Item ID {item_id} deleted.")
    except Exception as e:
        session.rollback()
        print(f"Error deleting item: {e}")
    finally:
        session.close()

def get_categories():
    session = get_session()
    try:
        categories = session.query(Category).all()
        return [(cat.id, cat.name) for cat in categories]
    finally:
        session.close()