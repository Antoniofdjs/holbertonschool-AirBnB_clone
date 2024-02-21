#!/usr/bin/python3


""" serializes instances to a JSON file
    and deserializes JSON file to instances
"""
import json


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns dictionary of objects {name.id: obj}"""
        return self.__objects

    def new(self, obj):
        """Add new instance to dictionary of __objects"""
        name_class = obj.__class__.__name__
        key_obj = str(name_class + "." + obj.id)
        self.__objects[key_obj] = obj

    def save(self):
        """ Dump dictionary __objects into file
            we take dictionary from object instead of putting object
            {classname.id:{object dictionary...},classname.id:{obj dict...}}
        """
        with open(self.__file_path, 'w') as f:
            dictionary_for_json = {}
            for key, obj in self.__objects.items():
                dictionary_for_json[key] = obj.to_dict()
            json.dump(dictionary_for_json, f)

    def reload(self):
        """ Loads the json file back into __objects
            creating the instances again and saving them into __objects
        """
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, 'r') as f:
                dictionary_from_json = json.load(f)
                for key, obj_dictionary in dictionary_from_json.items():
                    self.__objects[key] = BaseModel(**obj_dictionary)
        except FileNotFoundError:
            pass
