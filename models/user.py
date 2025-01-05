#!/usr/bin/python3
"""
This module defines a class User
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv

class User(BaseModel, base):
    """
    This class defines a user by various attributes
    """
    __tablename__ = users

    if getenv(HBNB_TYPE_STORAGE, default="fs") == "db":
        email = column(String(128), nullable=False)
        password = column(String(128), nullable=False)
        first_name = column(String(128), nullable=True)
        last_name = column(String(128), nullable=True)
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
