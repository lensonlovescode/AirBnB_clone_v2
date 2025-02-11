#!/usr/bin/python3
"""
Contains the DBStorage engine
"""

from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage():
    """
    Class definition Database storage engine
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes the DBStorage engine
        """
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST', 'localhost')
        database = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')
        eng = f"mysql+mysqldb://{user}:{password}@{host}/{database}"

        self.__engine = create_engine(eng, pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """"
        Query on the current database session all
        objects depending on class name
        """
        objects = {}
        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            query = self.__session.query(cls)
            for obj in query:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj
        else:
            classes = [User, State, City, Amenity, Place, Review]
            for element in classes:
                query = self.__session.query(element)
                for obj in query:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objects[key] = obj

        return objects

    def new(self, obj):
        """
        Add an object to the current database session
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        Commit all changes to the database
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete an object from the database session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Reload data and setup the database session
        """
        from models.base_model import Base
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """
        calls remove()
        """
        self.__session.remove()
