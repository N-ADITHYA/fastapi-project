from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import Relationship
from sqlalchemy_db import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    owner = Relationship('User')

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, nullable=False, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=True, server_default=text('now()'))
    phone_number = Column(String, nullable=True)
class Vote(Base):
    __tablename__ = 'votes'
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id', ondelete='CASCADE'), primary_key=True)