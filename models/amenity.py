#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String

class Amenity(BaseModel, Base):
    """
    An amenity
    """

    __tablename__ = "amenities"

    if getenv('HBNB_TYPE_STORAGE', default='fs') == 'db':
        
        name = Column(String(128), nullable=False)
    else:
        name = ""