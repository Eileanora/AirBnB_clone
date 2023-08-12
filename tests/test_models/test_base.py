#!/usr/bin/python3
'''Module for testing the base_model class'''
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
from time import sleep


class TestBase(unittest.TestCase):
    '''Tests for the BaseModel class attributes and init'''

    def test_init_no_args(self):
        '''Test for init method with no arguments'''
        b = BaseModel()
        self.assertTrue(isinstance(b, BaseModel))
        self.assertTrue(hasattr(b, 'id'))
        self.assertTrue(hasattr(b, 'created_at'))
        self.assertTrue(hasattr(b, 'updated_at'))
        self.assertTrue(type(b.created_at) is datetime)
        self.assertTrue(type(b.updated_at) is datetime)
        self.assertTrue(type(b.id) is str)
        self.assertTrue(b.created_at != b.updated_at)

    def test_unique_attributes(self):
        '''Test for unique id and created_at attributes'''
        b1 = BaseModel()
        sleep(1)
        b2 = BaseModel()
        self.assertTrue(b1.id != b2.id)
        self.assertTrue(b1.created_at != b2.created_at)
        self.assertTrue(b1.updated_at != b2.updated_at)

    def test_init_kwargs(self):
        '''Test for init method with kwargs'''
        curr_time = datetime.now()
        curr_time_iso = curr_time.isoformat()
        b = BaseModel(
            id='123',
            created_at=curr_time_iso,
            updated_at=curr_time_iso
            )
        self.assertTrue(isinstance(b, BaseModel))
        self.assertEqual(b.id, '123')
        self.assertEqual(b.created_at, curr_time)
        self.assertEqual(b.updated_at, curr_time)

    def test_init_with_kwargs_dict(self):
        '''Test for init method with kwargs'''
        b = BaseModel()
        b_dict = b.to_dict()
        b2 = BaseModel(**b_dict)
        self.assertTrue(isinstance(b2, BaseModel))
        self.assertTrue(b is not b2)
        self.assertEqual(b.id, b2.id)
        self.assertEqual(b.created_at, b2.created_at)
        self.assertEqual(b.updated_at, b2.updated_at)

    def test_init_with_kwargs_extra(self):
        '''Test for init method with kwargs'''
        b = BaseModel()
        b_dict = b.to_dict()
        b_dict["new_attr"] = 1234
        b2 = BaseModel(**b_dict)
        self.assertTrue(hasattr(b2, 'new_attr'))

    def test_str(self):
        '''Test for __str__ method'''
        b = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(b.id, b.__dict__)
        self.assertEqual(str(b), expected_str)

    def test_save(self):
        '''Test for save method'''
        b = BaseModel()
        first_updated_at = b.updated_at
        sleep(1)
        b.save()
        second_updated_at = b.updated_at
        self.assertTrue(first_updated_at != second_updated_at)

    def test_to_dict(self):
        b = BaseModel()
        base_model_dict = b.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertEqual(base_model_dict['id'], b.id)
        self.assertEqual(
            base_model_dict['created_at'],
            b.created_at.isoformat()
            )
        self.assertEqual(
            base_model_dict['updated_at'],
            b.updated_at.isoformat()
            )

    if __name__ == '__main__':
        unittest.main()
