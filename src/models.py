import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table address.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    phone_num = Column(Integer)
    email = Column(String(250))
    address = Column(String(250))

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    id = Column(Integer, primary_key=True)
    photo_id = Column(Integer)
    post_date = Column(Integer)
    content = Column(String(250))

class Tag(Base):
    __tablename__ = 'tag'
    # Here we define columns for the table address.
    id = Column(Integer, primary_key=True)
    photo_id = Column(Integer)
    title = Column(String(250))
    

class Album(Base):
    __tablename__ = 'album'
    # Here we define columns for the table address.
    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    description = Column(String(250))
    views = Column(Integer)

class Location(Base):
    __tablename__ = 'location'
    # Here we define columns for the table address.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    short_name = Column(String(250))
   
class Photo(Base):
    __tablename__ = 'photo'
    # Here we define columns for the table address.
    id = Column(Integer, primary_key=True)
    album_id = Column(Integer, ForeignKey('album.id'))
    location_id = Column(Integer, ForeignKey('location.id'))
    tag_id = Column(Integer, ForeignKey('tag.id'))
    comment_id = Column(Integer, ForeignKey('comment.id'))
    follower_id = Column(Integer, ForeignKey('follower.id'))
    album = relationship(Album)
    location = relationship(Location)
    tag = relationship(Tag)
    comment = relationship(Comment)
    follower = relationship(Follower)
  


    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')