#!/usr/bin/python3


import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    
    def test_name(self):
        new_state= State()
        new_state.name = "texas"
        self.assertEqual(new_state.name, "texas")

    def test_id(self):
        s1 = State()
        s2 = State()
        self.assertIsInstance(s1, BaseModel)
        self.assertTrue(hasattr(s1, "id"))
        self.assertNotEqual(s1.id, s2.id)
        self.assertIsInstance(s1.id, str)

if __name__ == '__main__':

    unittest.main()
