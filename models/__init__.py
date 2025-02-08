#!/usr/bin/python3
"""
This script create a unique FileStorage instance for the Airbnnb application
"""
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
# """This module instantiates an object of class FileStorage"""
# from models.engine.file_storage import FileStorage
# from models.engine.db_storage import DBStorage
# from models.base_model import BaseModel
# from models.user import User
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.place import Place
# from models.review import Review
# from os import getenv

# storage_type = getenv('HBNB_TYPE_STORAGE')

# if storage_type == 'db':
#     storage = DBStorage()
# else:
#     storage = FileStorage()

# storage.reload()
