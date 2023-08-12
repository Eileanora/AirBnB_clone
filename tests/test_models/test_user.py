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

    def test_class_attributes_exist(self):
        '''Test for class attributes'''
        u = User()
        self.assertTrue(hasattr(User, 'email'))
        self.assertTrue(hasattr(User, 'password'))
        self.assertTrue(hasattr(User, 'first_name'))
        self.assertTrue(hasattr(User, 'last_name'))

    def test_class_attributes_type(self):
        '''Test for class attributes'''
        self.assertTrue(type(User.email) is str)
        self.assertTrue(type(User.password) is str)
        self.assertTrue(type(User.first_name) is str)
        self.assertTrue(type(User.last_name) is str)

    def test_class_attributes_default(self):
        '''Test for class attributes'''
        self.assertEqual(User.email, '')
        self.assertEqual(User.password, '')
        self.assertEqual(User.first_name, '')
        self.assertEqual(User.last_name, '')


if __name__ == '__main__':
    unittest.main()
