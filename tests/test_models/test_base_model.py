#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    '''Tests for the BaseModel class'''
    
    def setUp(self):
        '''Set up testing environment'''
        self.b = BaseModel()
        self.b.name = "btats"
        self.b.save()
    
    def tearDown(self):
        '''Tear down testing environment'''
        del self.b
    
    def test_init(self):
        '''Test constructor'''
        self.assertTrue(isinstance(self.b, BaseModel))