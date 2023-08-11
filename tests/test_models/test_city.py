#!/usr/bin/python3
'''Unittests for the city class'''
from models.city import City
from tests.test_models.test_base_model import TestBase
import unittest


class TestCity(TestBase):
    '''Tests for the City class'''
    def setUp(self):
        '''Set up method'''
        super().setUp()
        self.cls = City

    def test_class_attributes(self):
        '''Test for class attributes'''
        c = City()
        self.assertTrue(hasattr(c, 'state_id'))
        self.assertTrue(type(c.state_id) is str)
        self.assertTrue(hasattr(c, 'name'))
        self.assertTrue(type(c.name) is str)


if __name__ == '__main__':
    unittest.main()
