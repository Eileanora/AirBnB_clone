#!usr/bin/python3
'''Module for testing the place class'''
import unittest
from models.place import Place
from tests.test_models.test_base_model import TestBase


class TestPlace(TestBase):
    '''Tests for the Place class'''
    def setUp(self):
        '''Set up method'''
        super().setUp()
        self.cls = Place

    def test_class_attributes(self):
        '''Test for class attributes'''
        p = Place()
        self.assertTrue(hasattr(p, 'city_id'))
        self.assertTrue(hasattr(p, 'user_id'))
        self.assertTrue(hasattr(p, 'name'))
        self.assertTrue(hasattr(p, 'description'))
        self.assertTrue(hasattr(p, 'number_rooms'))
        self.assertTrue(hasattr(p, 'number_bathrooms'))
        self.assertTrue(hasattr(p, 'max_guest'))
        self.assertTrue(hasattr(p, 'price_by_night'))
        self.assertTrue(hasattr(p, 'latitude'))
        self.assertTrue(hasattr(p, 'longitude'))
        self.assertTrue(hasattr(p, 'amenity_ids'))
        self.assertEqual(p.city_id, '')
        self.assertEqual(p.user_id, '')
        self.assertEqual(p.name, '')
        self.assertEqual(p.description, '')
        self.assertEqual(p.number_rooms, 0)
        self.assertEqual(p.number_bathrooms, 0)
        self.assertEqual(p.max_guest, 0)
        self.assertEqual(p.price_by_night, 0)
        self.assertEqual(p.latitude, 0.0)
        self.assertEqual(p.longitude, 0.0)
        self.assertEqual(p.amenity_ids, [""])


if __name__ == '__main__':
    unittest.main()
