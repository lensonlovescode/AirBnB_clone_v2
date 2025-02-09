#!/usr/bin/python3
"""
This is the state class
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.city import City
from sqlalchemy.orm import relationship
from os import getenv

#  getter attribute cities that returns the list of City instances with state_id equals
#     to the current State.id => It will be the FileStorage relationship between State and City

class State(BaseModel, Base):
    """
    State class
    """
    
    __tablename__ = 'states'
    
    if getenv('HBNB_TYPE_STORAGE', default='fs') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete')

    else:
        name = ""
        
        @property
        def cities(self):
            """
            Return a list of City instances with matching state_id
            """
            from models import storage
            city_list = []
            for city in storage.all('City').values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list

    # @property
    # def cities(self):
    #     var = models.storage.all()
    #     lista = []
    #     result = []
    #     for key in var:
    #         city = key.replace('.', ' ')
    #         city = shlex.split(city)
    #         if (city[0] == 'City'):
    #             lista.append(var[key])
    #     for elem in lista:
    #         if (elem.state_id == self.id):
    #             result.append(elem)
    #     return (result)
