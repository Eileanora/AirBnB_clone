#!/usr/bin/python3
'''Module for testing the file storage'''
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.__init__ import storage


class TestFileStorage(unittest.TestCase):
    '''Tests for the file storage class'''
    def test_