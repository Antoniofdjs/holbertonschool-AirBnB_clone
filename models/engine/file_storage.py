#!/usr/bin/python3


""" serializes instances to a JSON file
    and deserializes JSON file to instances
"""
import json


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        name_class = obj.__class__.__name__
        key_obj = str(name_class + "." + obj.id)
        self.__objects[key_obj] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            dictionary_for_json = {}
            for key, obj in self.__objects.items():
                dictionary_for_json[key] = obj.to_dict()
            json.dump(dictionary_for_json, f)

    def reload(self):
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, 'r') as f:
                dictionary_from_json = json.load(f)
                for key, obj_dictionary in dictionary_from_json.items():
                    self.__objects[key] = BaseModel(**obj_dictionary)
        except FileNotFoundError:
            pass
