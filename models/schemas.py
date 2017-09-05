from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy import Index
from sqlalchemy.orm import relationship, backref
import psycopg2
Base = declarative_base()
from sqlalchemy import *
current_connection = create_engine(
    "postgres://postgres:kenyanya19@127.0.0.1/postgres")


class User(Base):
    __tablename__ = 'user'
    user_id = Column(String(250), index=True, primary_key=True)
    username = Column(String(250))
    emailaddress = Column(String)
    password = Column(String)


class ShoppingList(Base):
    __tablename__ = 'shoppinglist'
    name = Column(String(40), primary_key=True)
    items = relationship('Items', backref='shoppinglist')


class Items(Base):
    __tablename__ = 'items'
    category_id = Column(Integer, primary_key=True)
    restaurant_id = Column(String(250))


Base.metadata.create_all(current_connection)
