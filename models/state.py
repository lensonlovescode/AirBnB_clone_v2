#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage_type
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if storage_type == "db":
        # Database storage: establish relationship with City
        cities = relationship(
            "City",
            backref='state',
            cascade='all, delete, delete-orphan'
        )
    else:
        @property
        def cities(self):
            """Returns a list of City instances with state_id equal to the current State.id."""
            from models import storage
            all_cities = storage.all(City)
            return [city for city in all_cities.values() if city.state_id == self.id]
