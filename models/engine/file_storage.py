#!/usr/bin/python3
'''Module for file storage class'''
import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

class FileStorage:
    '''Class that serializes instances to a JSON file \
and deserializes JSON file to instances'''
    __file_path = 'data.json'
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return FileStorage.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        dic_obj = {}
        
        for k, v in FileStorage.__objects.items():
            dic_obj[k] = v.to_dict()
        
        with open(FileStorage.__file_path, mode= "w", encoding="utf-8") as f:
            json.dump(dic_obj, f)
    
    def reload(self):
        '''deserializes the JSON file to __objects if the file exists'''
        if os.path.isfile(FileStorage.__file_path) and os.path.getsize(FileStorage.__file_path) > 0:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                data = json.load(f)
                for k, v in data.items():
                    FileStorage.__objects[k] = eval(v['__class__'])(**v)
