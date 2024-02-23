#!/usr/bin/python3
"""Test module for State class"""
import unittest
from models.state import State

class TestState(unittest.TestCase):
    """Test cases for State class"""

    def test_instance_creation(self):
        """Test creation of State instance"""
        state = State()
        self.assertIsInstance(state, State)
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertTrue(hasattr(state, 'name'))

    def test_to_dict_method(self):
        """Test to_dict method of State class"""
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)

    def test_str_method(self):
        """Test __str__ method of State class"""
        state = State()
        str_rep = str(state)
        self.assertIsInstance(str_rep, str)
        self.assertIn('State', str_rep)
        self.assertIn(state.id, str_rep)

if __name__ == '__main__':
    unittest.main()