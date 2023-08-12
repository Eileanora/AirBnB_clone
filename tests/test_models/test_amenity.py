#!/usr/bin/python3
'''Unittests for the amenity class'''
from models.amenity import Amenity
from tests.test_models.test_base_model import TestBase
import unittest


class TestAmenity(TestBase):
    '''Tests for the Amenity class'''
    def setUp(self):
        '''Set up method'''
        super().setUp()
        self.cls = Amenity

    def test_class_attributes(self):
        '''Test for class attributes'''
        a = Amenity()
        self.assertTrue(hasattr(a, 'name'))
        self.assertTrue(type(a.name) is str)
        self.assertEqual(a.name, '')


if __name__ == '__main__':
    unittest.main()
