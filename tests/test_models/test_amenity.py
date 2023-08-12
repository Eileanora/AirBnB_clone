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

    def test_class_attributes_exist(self):
        '''Test for class attributes exist'''
        self.assertTrue(hasattr(Amenity, 'name'))

    def test_class_attributes_type(self):
        '''Test for class attributes type'''
        self.assertTrue(type(Amenity.name) is str)

    def test_class_attributes_default(self):
        '''Test for class attributes default'''
        self.assertEqual(Amenity.name, '')


if __name__ == '__main__':
    unittest.main()
