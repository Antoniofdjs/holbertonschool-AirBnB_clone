#!/usr/bin/python3


"""Defines all common atributes/methods for other classes"""

import uuid
import datetime
from models import storage


class BaseModel:

    def __init__(self, *args, **kwargs):

        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        kwargs.pop('__class__', None)  # __class__ removed from kwargs
        if kwargs:
            for attribute, value in kwargs.items():
                # Check date keys to remove isoformat from value
                if attribute == "created_at" or attribute == "updated_at":
                    setattr(self, attribute, datetime.datetime.strptime(
                        value, date_format))
                else:
                    setattr(self, attribute, value)

        else:
            id = uuid.uuid4()

            self.id = str(id)
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def to_dict(self):
        """returns dictionary of keys/values of __dict__ of the instance:"""
        dictionary = self.__dict__.copy()
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary['__class__'] = self.__class__.__name__
        return dictionary

    def save(self):
        """save new update date"""
        storage.save()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """str representation of obj"""
        class_name = self.__class__.__name__

        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
