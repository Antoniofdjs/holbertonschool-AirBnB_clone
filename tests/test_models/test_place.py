#!/usr/bin/python3


import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    
    def test_placeuserid_text(self):
        p = Place()
        p.city_id = "ponce"
        p.user_id = "123"
        p.name = "Place"
        p.description = "Description"
        p.number_rooms = 1
        p.number_bathrooms = 2
        p.max_guest = 3
        p.price_by_night = 4
        p.latitude = 5.6
        p.longitude = -7.8
        p.amenity_ids = ["9", "10", "11"]
        self.assertEqual(p.city_id, "ponce")
        self.assertEqual(p.user_id, "123")
        self.assertEqual(p.name, "Place")
        self.assertEqual(p.description, "Description")
        self.assertEqual(p.number_rooms, 1)
        self.assertEqual(p.number_bathrooms, 2)
        self.assertEqual(p.max_guest, 3)
        self.assertEqual(p.price_by_night, 4)
        self.assertEqual(p.latitude, 5.6)
        self.assertEqual(p.longitude, -7.8)
        self.assertListEqual(p.amenity_ids, ["9", "10", "11"])
        self.assertEqual(p.amenity_ids[0], "9")

    def test_id(self):
        p1 = Place()
        p2 = Place()
        self.assertIsInstance(p1, BaseModel)
        self.assertTrue(hasattr(p1, "id"))
        self.assertNotEqual(p1.id, p2.id)
        self.assertIsInstance(p1.id, str)

if __name__ == '__main__':

    unittest.main()
