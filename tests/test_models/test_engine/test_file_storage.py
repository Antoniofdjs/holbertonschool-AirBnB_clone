#!/usr/bin/python3
"""Test for base_model"""

import unittest
import json
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class Tests_uni(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()
        self.model = BaseModel()

    def test_all_method(self):
        """TESTING it Returns a dictionary of objects
            in format {""classname.id": object}
        """
        model_name_id = str(self.model.__class__.__name__) + "." + str(self.model.id)
        self.storage.new(self.model)

        my_dictionary = {}
        my_dictionary[model_name_id] = self.model  # {model_name_id : self.model}
        obect_dictionary = self.storage.all()

        self.assertDictEqual(my_dictionary, obect_dictionary)  # check if dicts are equal

    def test_file_path(self):
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")

    def test_new(self):
        """Test if new objects are added to __objects"""
        initial_count = len(self.storage.all())
        self.storage.new(BaseModel())
        self.storage.new(BaseModel())
        new_count = len(self.storage.all())
        self.assertNotEqual(initial_count, new_count)

    def test_save(self):
        """ Dump dictionary __objects into file
            we put dictionary from object
            {classname.id:{object dictionary...},classname.id:{obj dict...}}
        """
        self.model.name = "Test Model"
        self.model.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r") as f:
            data = json.load(f)
            key = f"BaseModel.{self.model.id}"
            self.assertIn(key, data)
            self.assertEqual(data[key]["name"], "Test Model")

    def test_reload(self):
        """Reload from .sjon file test to rereate list of objects"""
        self.assertTrue(len(self.storage.all()) > 0)
        self.model.save()
        with open("file.json", "r") as f:
            data = json.load(f)
        key = f"BaseModel.{self.model.id}"
        data[key]['custom_attribute'] = "Test Reload"
        with open("file.json", "w") as f:
            json.dump(data, f)
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertIn(key, all_objects)
        loaded_model = all_objects[key]
        self.assertTrue('custom_attribute' in loaded_model.to_dict())
        self.assertEqual(loaded_model.to_dict()['custom_attribute'], "Test Reload")

if __name__ == '__main__':

    unittest.main()
