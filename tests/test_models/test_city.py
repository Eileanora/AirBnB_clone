#!/usr/bin/python3
'''Unittests for the city class'''
from models.city import City
from tests.test_models.test_base_model import TestBase
import unittest


class TestCity(TestBase):
    '''Tests for the City class'''
    def setUp(self):
        '''Set up method'''
        self.cls = City
        super().setUp()

    def test_class_attributes_exist(self):
        '''Test for class attributes'''
        self.assertTrue(hasattr(City, 'state_id'))
        self.assertTrue(hasattr(City, 'name'))

    def test_class_attributes_type(self):
        '''Test for class attributes'''
        self.assertTrue(type(City.state_id) is str)
        self.assertTrue(type(City.name) is str)

    def test_class_attributes_default(self):
        '''Test for class attributes'''
        self.assertEqual(City.state_id, '')
        self.assertEqual(City.name, '')


if __name__ == '__main__':
    unittest.main()
