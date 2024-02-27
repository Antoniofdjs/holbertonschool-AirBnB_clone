#!/usr/bin/python3


"""Defines all common atributes/methods for other classes"""

import uuid
import datetime
from models import storage


class BaseModel:

    def __init__(self, *args, **kwargs):
        """
            Inits the id, created_at, and updated_at instance attributes
            Saves the new instance in the dict of file_storage.py, __objects
            If kwargs detected, object is not saved, in __objects since ...
            it comes from the json.file.
            For kwargs we recreate the instance but no saves occur

            Example: BaseModel(**dict_from_json) -- Recreate instance
            Example: BaseModel() -- Create new instance and save
        """

        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        kwargs.pop('__class__', None)  # __class__ removed from kwargs

        if kwargs:  # Recreate instance from json.file
            for attribute, value in kwargs.items():

                # Check date keys to remove isoformat from value
                if attribute == "created_at" or attribute == "updated_at":
                    setattr(self, attribute, datetime.datetime.strptime(
                        value, date_format))
                else:
                    setattr(self, attribute, value)

        else:  # New instance
            id = uuid.uuid4()  # Random id generator

            self.id = str(id)
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)  # Add new object to storage '__objects'

    def to_dict(self):
        """
            returns dictionary of instance (__dict__)
            to this dict we also add __class__
        """

        dictionary = self.__dict__.copy()
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary['__class__'] = self.__class__.__name__

        return dictionary

    def save(self):
        """
            save new updated_at date and save data to json.file
        """
        self.updated_at = datetime.datetime.now()
        storage.save()  # Save changes to json.file

    def __str__(self):
        """
            str representation of instance
        """
        class_name = self.__class__.__name__

        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
