#!/usr/bin/env python3
'''Module for file storage class'''
import json
from models.base_model import BaseModel
import os.path


class FileStorage:
    '''Class that serializes instances to a JSON file \
and deserializes JSON file to instances'''
    __file_path = 'file.json'
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
        with open(self, __file_path, 'w') as f:
            json.dump(FileStorage.__objects, f)
    
    def reload(self):
        '''deserializes the JSON file to __objects if the file exists'''
        if os.path.isfile(self, __file_path):
            with open(self, __file_path, 'r') as f:
                FileStorage.__objects = json.load(f)
