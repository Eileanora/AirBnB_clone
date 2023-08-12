#!/usr/bin/python3
'''Module for testing the base_model class'''
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage
from datetime import datetime
from time import sleep
import os


class TestBase(unittest.TestCase):
    '''Base test class'''
    cls = User
    def setUp(self):
        '''Set up method'''
        self.obj = self.cls()
        FileStorage._FileStorage__file_path = 'test.json'
        f = open(FileStorage._FileStorage__file_path, "w")
        f.close()

    def tearDown(self):
        '''Tear down method'''
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)
        FileStorage._FileStorage__file_path = 'test.json'

    def test_init_no_args(self):
        '''Test for init method with no arguments'''
        self.assertTrue(isinstance(self.obj, self.cls))
        self.assertTrue(hasattr(self.obj, 'id'))
        self.assertTrue(hasattr(self.obj, 'created_at'))
        self.assertTrue(hasattr(self.obj, 'updated_at'))

    def test_unique_attributes(self):
        '''Test for unique id and created_at attributes'''
        b1 = self.cls()
        sleep(1)
        b2 = self.cls()
        self.assertTrue(b1.id != b2.id)
        self.assertTrue(b1.created_at != b2.created_at)
        self.assertTrue(b1.updated_at != b2.updated_at)

    def test_init_kwargs(self):
        '''Test for init method with kwargs'''
        curr_time = datetime.now()
        curr_time_iso = curr_time.isoformat()
        b = self.cls(id='123', created_at=curr_time_iso, updated_at=curr_time_iso)
        self.assertTrue(isinstance(b, self.cls))
        self.assertEqual(b.id, '123')
        self.assertEqual(b.created_at, curr_time)
        self.assertEqual(b.updated_at, curr_time)

    def test_init_with_kwargs_dict(self):
        '''Test for init method with kwargs'''
        b_dict = self.obj.to_dict()
        b2 = self.cls(**b_dict)
        self.assertTrue(isinstance(b2, self.cls))
        self.assertTrue(self.obj is not b2)
        self.assertEqual(self.obj.id, b2.id)
        self.assertEqual(self.obj.created_at, b2.created_at)
        self.assertEqual(self.obj.updated_at, b2.updated_at)

    def test_init_with_kwargs_extra(self):
        '''Test for init method with kwargs'''
        b_dict = self.obj.to_dict()
        b_dict["new_attr"] = 1234
        b2 = self.cls(**b_dict)
        self.assertTrue(hasattr(b2, 'new_attr'))

    def test_str(self):
        '''Test for __str__ method'''
        expected_str = "[{}] ({}) {}".format(self.cls.__name__, self.obj.id, self.obj.__dict__)
        self.assertEqual(str(self.obj), expected_str)

    def test_save(self):
        '''Test for save method'''
        first_updated_at = self.obj.updated_at
        sleep(1)
        self.obj.save()
        second_updated_at = self.obj.updated_at
        self.assertTrue(first_updated_at != second_updated_at)

    def test_to_dict(self):
        '''Test for to_dict method'''
        base_model_dict = self.obj.to_dict()
        self.assertIsInstance(base_model_dict, dict)
