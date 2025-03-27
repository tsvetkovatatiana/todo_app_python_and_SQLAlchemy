from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///todo.db", echo=True, future=True)

# Items
class Item(Base):
    __tablename__ = "items"
    itemId = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    users = relationship("User", secondary="user_items", back_populates="items")

# Users
class User(Base):
    __tablename__ = "users"
    userId = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

    items = relationship("Item", secondary="user_items", back_populates="users")

# User's todos
class UserItem(Base):
    __tablename__ = "user_items"
    userId = Column(Integer, ForeignKey("users.userId"), primary_key=True)
    itemId = Column(Integer, ForeignKey("items.itemId"), primary_key=True)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
