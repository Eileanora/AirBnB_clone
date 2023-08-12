#!/usr/bin/python3
'''Unittests for the BaseModel class'''
from models.base_model import BaseModel
from tests.test_models.base import TestBase
import unittest


class TestBaseModel(TestBase):
    '''Tests for the BaseModel class'''

    def setUp(self):
        '''Set up method'''
        self.cls = BaseModel
        super().setUp()


if __name__ == '__main__':
    unittest.main()
