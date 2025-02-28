#!/usr/bin/python3
"""
This module defines a base class for all models in our hbnb clone
"""
import uuid
from datetime import datetime
from sqlalchemy import String, DateTime, Column
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    """
    A base class for all hbnb models
    """

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow,
                        onupdate=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """
        Returns a string representation of the instance
        """
        cls = self.__class__.__name__
        attrs = {k: v for k, v in self.__dict__.items()
                 if not k.startswith('_')}
        return '[{}] ({}) {}'.format(cls, self.id, attrs)

    def save(self):
        """
        Updates updated_at with current time when instance is changed
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})

        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary.pop('_sa_instance_state')
        return dictionary

    def delete(self):
        """
        Deletes the current instance from the storage
        (models.storage) by calling the method delete
        """
        from models import storage
        self.delete()
