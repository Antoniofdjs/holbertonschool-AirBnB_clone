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
        self.__objects[key_obj] = obj.to_dict()

    def save(self):
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
