#!/usr/bin/python3
"""Unitest module"""

import json
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class Test_FileStorage(unittest.TestCase):
    """Defines FileStorage class test cases"""
    
    
    def test_type(self):
        self.assertIsInstance(storage.all(), dict)
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)
        
    
    def test_newobj(self):
        my_model = BaseModel() 
        storage.new(my_model)       
        name = my_model.__class__.__name__
        key = name + '.' + my_model.id
        l_obj = storage.all()
        
        self.assertEqual(l_obj[key], my_model) 
        
    def test_save(self):
           my_model = BaseModel()
           storage.new(my_model)
           storage.save()
           f_text = ""
           with open("file.json", "r") as f:
               f_text = f.read()
               self.assertIn("BaseModel."+ my_model.id, f_text)
               
    def test_reload(self):
        my_model = BaseModel()
        storage.new(my_model)
        storage.save()
        storage.reload()
        l_obj = storage.all()
        self.assertIn("BaseModel." +my_model.id, l_obj.keys())
           
                   

if __name__ == '__main__':
    unittest.main()

