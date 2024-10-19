import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower (Base):
    __tablename__ = "Follower"
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer,ForeignKey("User.id"))
    user_to_id = Column(Integer,ForeignKey("User.id"))
    

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, unique=True)
    user_name = Column(String(250))
    first_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250), unique=True)

class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True, unique=True)
    user_id = Column(Integer, ForeignKey('User.id'))

class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True, unique=True)
    comment_text= Column(String(250))
    author_id = Column(Integer, ForeignKey('User.id'))
    post_id = Column(Integer, ForeignKey('Post.id'))


class Media(Base):
    __tablename__ = 'Media'
    id = Column(Integer, primary_key=True, unique=True)
    type = Column(String(250))
    url = Column(String(250))
    post_id= Column(Integer, ForeignKey('Post.id'))


try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
