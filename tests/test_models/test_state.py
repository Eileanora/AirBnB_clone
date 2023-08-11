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

    def test_class_attributes(self):
        '''Test for class attributes'''
        s = State()
        self.assertTrue(hasattr(s, 'name'))
        self.assertTrue(type(s.name) is str)


if __name__ == '__main__':
    unittest.main()
