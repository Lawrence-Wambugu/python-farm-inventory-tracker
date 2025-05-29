from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)  # e.g., Crops, Livestock, Equipment
    items = relationship("Item", back_populates="category")
    
    def __repr__(self):
        return f"<Category(name={self.name})>"

class Item(Base):
    __tablename__ = 'items'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)  # e.g., Wheat, Cow, Tractor
    quantity = Column(Float, nullable=False, default=0.0)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    category = relationship("Category", back_populates="items")
    transactions = relationship("Transaction", back_populates="item")
    
    def __repr__(self):
        return f"<Item(name={self.name}, quantity={self.quantity})>"

class Transaction(Base):
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    quantity = Column(Float, nullable=False)  # Positive for additions, negative for removals
    transaction_type = Column(String, nullable=False)  # e.g., 'add', 'remove'
    timestamp = Column(DateTime, default=datetime.utcnow)
    item = relationship("Item", back_populates="transactions")
    
    def __repr__(self):
        return f"<Transaction(item_id={self.item_id}, quantity={self.quantity}, type={self.transaction_type})>"