#!/usr/bin/python3
'''Module for testing the file storage'''
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.__init__ import storage
from os import path


class TestFileStorage_arrtibutes(unittest.TestCase):
    '''Tests for the FileStorage class attributes and init'''
    def setUp(self):
        '''Set up method'''
        self.storage = FileStorage()

    def test_init_no_args(self):
        '''Test for init method with no arguments'''
        store = FileStorage()
        self.assertTrue(isinstance(self.storage, FileStorage))

    def test_init_arges(self):
        '''Test for init method with arguments'''
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_File_not_exist(self):
        '''Test for __file_path does not exist'''
        newpath = "test.json"
        if (not path.isfile(newpath)):
            pass

    def test_File_exist_empty(self):
        '''Test for __file_path exist but is empty'''
        newpath = "test.json"
        if (path.isfile(newpath) and path.getsize() <= 0):
            pass

    def test_path_is_private_str(self):
        '''Test for __file_path attribute'''
        with self.assertRaises(AttributeError):
            print(FileStorage.__file_path)
        self.assertEqual(dict, type(self.storage._FileStorage__objects))

    def test_objects_is_private_dict(self):
        '''Test for __objects attribute'''
        with self.assertRaises(AttributeError):
            print(FileStorage.__objects)
        self.assertEqual(dict, type(self.storage._FileStorage__objects))


class TestFileStorage_methods(unittest.TestCase):
    '''Tests for the FileStorage class methods'''
    def setUp(self):
        '''Set up method'''
        self.storage = FileStorage()
    
    def test_all(self):
        '''Test for all method'''
        self.assertEqual(dict, type(self.storage.all()))
    
    def test_new(self):
        '''Test for new method'''
        self.storage.new(BaseModel())
        self.assertEqual(dict, type(self.storage.all()))
    
    def test_save(self):
        '''Test for save method'''
        pass
    
    def test_reload(self):
        '''Test for reload method'''
        pass

if __name__ == '__main__':
    unittest.main()
