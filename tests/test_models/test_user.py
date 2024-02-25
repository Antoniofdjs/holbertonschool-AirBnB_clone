#!/usr/bin/python3
'''
    test_state.py
    
    Unittest
'''
import unittest
from models.user import User
from models.base_model import BaseModel


class test_state(unittest.TestCase):
    '''
        Class State Unittest
    '''
    def test_user(self):
        u = User()
        u.email = "@test"
        u.password= "123"
        u.first_name = "ant"
        u.last_name = "dejesus"
        self.assertEqual(u.email, "@test")
        self.assertEqual(u.password, "123")
        self.assertEqual(u.first_name, "ant")
        self.assertEqual(u.last_name, "dejesus")

    def test_id(self):
        u1 = User()
        u2 = User()
        self.assertIsInstance(u1, BaseModel)
        self.assertTrue(hasattr(u1, "id"))
        self.assertNotEqual(u1.id, u2.id)
        self.assertIsInstance(u1.id, str)


if __name__ == '__main__':
    unittest.main()
