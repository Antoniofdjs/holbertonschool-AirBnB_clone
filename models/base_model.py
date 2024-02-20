#!/usr/bin/python3


"""Defines all common atributes/methods for other classes"""

import uuid
import datetime


class BaseModel:

    def __init__(self):
        id = uuid.uuid4()

        self.id = str(id)
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns dictionary of keys/values of __dict__ of the instance:"""
        dictionary = self.__dict__.copy()
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary['__class__'] = self.__class__.__name__
        return dictionary

    def save(self):
        """save new update date""" 
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """str representation of obj"""
        class_name = self.__class__.__name__

        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
