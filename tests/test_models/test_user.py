#!/usr/bin/python3
'''
    test_user.py
    
    Unittest
'''
import unittest
from models.user import User


class test_user(unittest.TestCase):
    '''
        Class User Unittest
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
        self.assertTrue(hasattr(u1, "id"))
        self.assertNotEqual(u1.id, u2.id)
        self.assertIsInstance(u1.id, str)


if __name__ == '__main__':
    unittest.main()
