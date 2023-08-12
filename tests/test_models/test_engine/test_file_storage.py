#!/usr/bin/python3
'''Module for testing the file storage'''
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.__init__ import storage
from os import path
import os


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
        FileStorage._FileStorage__file_path = 'test.json'
        f = open(FileStorage._FileStorage__file_path, "w")
        f.close()
        self.storage = FileStorage()
        self.u = User()
        self.b = BaseModel()
        self.s = State()
        self.c = City()
        self.a = Amenity()
        self.p = Place()
        self.r = Review()

    def tearDown(self):
        '''Tear down method'''
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)
        FileStorage._FileStorage__file_path = 'test.json'

    def test_all(self):
        '''Test for all method'''
        self.assertEqual(dict, type(self.storage.all()))

    def new_func(self, obj):
        '''Test for new method'''
        new = obj()
        self.storage.new(new)
        key = type(new).__name__ + '.' + new.id
        self.assertTrue(key in self.storage.all())

    def test_new(self):
        '''Tests for the new method'''
        self.new_func(BaseModel)
        self.new_func(User)
        self.new_func(State)
        self.new_func(City)
        self.new_func(Amenity)
        self.new_func(Place)
        self.new_func(Review)

    def test_save(self):
        '''Test for save method'''
        self.storage.save()
        tmp = ""
        with open(FileStorage._FileStorage__file_path, 'r') as f:
            tmp = f.read()
            self.assertIn('BaseModel.' + self.b.id, tmp)
            self.assertIn('User.' + self.u.id, tmp)
            self.assertIn('State.' + self.s.id, tmp)
            self.assertIn('City.' + self.c.id, tmp)
            self.assertIn('Amenity.' + self.a.id, tmp)
            self.assertIn('Place.' + self.p.id, tmp)
            self.assertIn('Review.' + self.r.id, tmp)
        f.close()

    def test_reload(self):
        '''Test for reload method'''
        self.storage.save()
        self.storage.reload()
        dict_obj = FileStorage._FileStorage__objects
        self.assertIn('BaseModel.' + self.b.id, dict_obj)
        self.assertIn('User.' + self.u.id, dict_obj)
        self.assertIn('State.' + self.s.id, dict_obj)
        self.assertIn('City.' + self.c.id, dict_obj)
        self.assertIn('Amenity.' + self.a.id, dict_obj)
        self.assertIn('Place.' + self.p.id, dict_obj)
        self.assertIn('Review.' + self.r.id, dict_obj)

    def test_new_excess_args(self):
        '''Test for new method with excess arguments'''
        with self.assertRaises(TypeError):
            self.storage.new(BaseModel(), None)

    def test_new_no_args(self):
        '''Test for new method with no arguments'''
        with self.assertRaises(TypeError):
            self.storage.new()

    def test_save_excess_args(self):
        '''Test for save method with excess arguments'''
        with self.assertRaises(TypeError):
            self.storage.save(None)

    def test_reload_excess_args(self):
        '''Test for reload method with excess arguments'''
        with self.assertRaises(TypeError):
            self.storage.reload(None)


if __name__ == '__main__':
    unittest.main()
