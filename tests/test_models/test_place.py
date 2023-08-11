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
        self.assertTrue(type(p.city_id) is str)
        self.assertTrue(type(p.user_id) is str)
        self.assertTrue(type(p.name) is str)
        self.assertTrue(type(p.description) is str)
        self.assertTrue(type(p.number_rooms) is int)
        self.assertTrue(type(p.number_bathrooms) is int)
        self.assertTrue(type(p.max_guest) is int)
        self.assertTrue(type(p.price_by_night) is int)
        self.assertTrue(type(p.latitude) is float)
        self.assertTrue(type(p.longitude) is float)
        self.assertTrue(type(p.amenity_ids) is list)


if __name__ == '__main__':
    unittest.main()
