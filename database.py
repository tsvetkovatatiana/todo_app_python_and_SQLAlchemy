from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime

from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///todo.db", future=True)


# Notes
class Note(Base):
    __tablename__ = "notes"
    noteId = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    timeAdded = Column(DateTime, default=datetime.now())  # Used AI here, because it was the fastest way to check
    # The owner of the note (Primary owner)
    ownerId = Column(Integer, ForeignKey("users.userId"), nullable=False)

    # and with owner I used help, because I stuck with many-to-many kind of relationship and note
    # that need to have unique owner, so I interpreted it as a primary owner.
    # So users can share a note with a primary owner of that note
    owner = relationship("User", foreign_keys=[ownerId])
    users = relationship("User", secondary="user_notes", back_populates="notes")

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
