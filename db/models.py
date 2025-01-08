from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Float
from sqlalchemy.orm import relationship
from datetime import datetime


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=True)
    phone_number = Column(String, nullable=False, unique=True)
    age = Column(Integer, nullable=True)
    city = Column(String, nullable=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    reg_date = Column(DateTime, default=datetime.now())
    addresses = relationship('Address', back_populates='user')


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    pr_name = Column(String, nullable=False)
    pr_description = Column(String, nullable=True)
    pr_price = Column(Float, nullable=False)
    created_date = Column(DateTime, default=datetime.now())
    pr_likes = Column(Integer, default=0)
    pr_quantity = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.id'))

    user_id_fk = relationship(User, lazy='subquery')
    category = relationship('Category', back_populates='products', lazy='subquery')
class Cart(Base):
    __tablename__ = 'cart'

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    pr_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False)

    user_id_fk = relationship(User, lazy='subquery')
    pr_id_fk = relationship(Product, lazy='subquery')

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    total_price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    status = Column(String(50))

    user = relationship('User', lazy='subquery')
    order_items = relationship('OrderItem', lazy='subquery')

class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

    order_id_fk = relationship(Order, lazy='subquery')
    product_id_fk = relationship(Product, lazy='subquery')

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, autoincrement=True, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    text = Column(String, nullable=True)
    reg_date = Column(String, default=datetime.now())
    likes = Column(Integer, default=0)

    user_id_fk = relationship(User, lazy='subquery')
    product_id_fk = relationship(Product, lazy='subquery')

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=True)

    products = relationship("Product", back_populates="category")

class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    street = Column(String, nullable=False)
    house_number = Column(String, nullable=False)
    entrance_number = Column(String, nullable=True)
    apartment_number = Column(String, nullable=True)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)

    user = relationship('User', back_populates='addresses')

class PromoCode(Base):
    __tablename__ = 'promo_codes'

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    amount = Column(Float)
    min_order_value = Column(Float)