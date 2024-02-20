#!/usr/bin/python3
"""Test for base_model"""
import unittest
import uuid
import datetime
from models.base_model import BaseModel


class Tests_uni(unittest.TestCase):

    def test_save(self):
        obj = BaseModel()
        updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(updated_at, obj.updated_at)
        self.assertFalse(obj.updated_at is datetime)

    def test_init(self):
        """Test creations and init"""
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)
        self.assertTrue(uuid.UUID(my_model.id))

    def test_to_dictionary(self):
        """test if dictionary returned is correct from object"""
        new_model = BaseModel()
        id_compare = new_model.id
        created_at_compare = new_model.created_at.isoformat()
        updated_at_compare = new_model.updated_at.isoformat()

        compare_dictionary = {
            'id': id_compare,
            'created_at': created_at_compare,
            'updated_at': updated_at_compare,
            '__class__': 'BaseModel'
            }
        self.assertEqual(new_model.to_dict(), compare_dictionary)

    def test_str(self):
        """test str representation"""
        another_model = BaseModel()
        id = another_model.id
        self.assertEqual(str(another_model), "[BaseModel] ({}) {}".format(id, another_model.__dict__))


if __name__ == '__main__':

    unittest.main()
