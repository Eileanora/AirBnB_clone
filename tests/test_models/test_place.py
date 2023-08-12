#!usr/bin/python3
'''Module for testing the place class'''
import unittest
from models.place import Place
from tests.test_models.test_base_model import TestBase


class TestPlace(TestBase):
    '''Tests for the Place class'''
    def setUp(self):
        '''Set up method'''
        self.cls = Place
        super().setUp()

    def test_class_attributes_exist(self):
        '''Test for class attributes'''
        self.assertTrue(hasattr(Place, 'city_id'))
        self.assertTrue(hasattr(Place, 'user_id'))
        self.assertTrue(hasattr(Place, 'name'))
        self.assertTrue(hasattr(Place, 'description'))
        self.assertTrue(hasattr(Place, 'number_rooms'))
        self.assertTrue(hasattr(Place, 'number_bathrooms'))
        self.assertTrue(hasattr(Place, 'max_guest'))
        self.assertTrue(hasattr(Place, 'price_by_night'))
        self.assertTrue(hasattr(Place, 'latitude'))
        self.assertTrue(hasattr(Place, 'longitude'))
        self.assertTrue(hasattr(Place, 'amenity_ids'))

    def test_class_attributes_type(self):
        '''Test for class attributes type'''
        self.assertTrue(type(Place.city_id) is str)
        self.assertTrue(type(Place.user_id) is str)
        self.assertTrue(type(Place.name) is str)
        self.assertTrue(type(Place.description) is str)
        self.assertTrue(type(Place.number_rooms) is int)
        self.assertTrue(type(Place.number_bathrooms) is int)
        self.assertTrue(type(Place.max_guest) is int)
        self.assertTrue(type(Place.price_by_night) is int)
        self.assertTrue(type(Place.latitude) is float)
        self.assertTrue(type(Place.longitude) is float)
        self.assertTrue(type(Place.amenity_ids) is list)

    def test_class_attributes_default(self):
        '''Test for class attributes default'''
        self.assertEqual(Place.city_id, '')
        self.assertEqual(Place.user_id, '')
        self.assertEqual(Place.name, '')
        self.assertEqual(Place.description, '')
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [""])


if __name__ == '__main__':
    unittest.main()
