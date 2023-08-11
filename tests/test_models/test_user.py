#!/usr/bin/python3
'''Unittests for the User class'''
from models.user import User
from tests.test_models.test_base_model import TestBase
import unittest


class TestUser(TestBase):
    '''Tests for the User class'''
    def setUp(self):
        '''Set up method'''
        super().setUp()
        self.cls = User

    def test_class_attributes(self):
        '''Test for class attributes'''
        u = User()
        self.assertTrue(hasattr(u, 'email'))
        self.assertTrue(hasattr(u, 'password'))
        self.assertTrue(hasattr(u, 'first_name'))
        self.assertTrue(hasattr(u, 'last_name'))


if __name__ == '__main__':
    unittest.main()
