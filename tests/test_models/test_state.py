#!usr/bin/python3
'''Module for testing the state class'''
import unittest
from models.state import State
from tests.test_models.test_base_model import TestBase


class TestState(TestBase):
    '''Tests for the State class'''
    def setUp(self):
        '''Set up method'''
        super().setUp()
        self.cls = State

    def test_class_attributes_exist(self):
        '''Test for class attributes'''
        self.assertTrue(hasattr(State, 'name'))

    def test_class_attributes_type(self):
        '''Test for class attributes'''
        self.assertTrue(type(State.name) is str)

    def test_class_attributes_default(self):
        '''Test for class attributes'''
        self.assertEqual(State.name, '')


if __name__ == '__main__':
    unittest.main()
