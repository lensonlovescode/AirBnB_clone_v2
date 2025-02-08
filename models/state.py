#!/usr/bin/python3
"""This is the state class"""
# from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel
# from sqlalchemy.orm import relationship
# from sqlalchemy import Column, Integer, String
# import models
# from models.city import City
# import shlex

class State(BaseModel):
    """ State class """
    name = ""

# class State(BaseModel, Base):
#     """This is the class for State
#     Attributes:
#         name: input name
#     """
#     __tablename__ = "states"
#     name = Column(String(128), nullable=False)
#     cities = relationship('City',backref='state', cascade='all, delete')

#     # @property
#     # def cities(self):
#     # """Return a list of City instances with matching state_id."""
#     #     from models import storage
#     #     city_list = []
#     #     for city in storage.all('City').values():
#     #         if city.state_id == self.id:
#     #             city_list.append(city)
#     #     return city_list

#     @property
#     def cities(self):
#         var = models.storage.all()
#         lista = []
#         result = []
#         for key in var:
#             city = key.replace('.', ' ')
#             city = shlex.split(city)
#             if (city[0] == 'City'):
#                 lista.append(var[key])
#         for elem in lista:
#             if (elem.state_id == self.id):
#                 result.append(elem)
#         return (result)
