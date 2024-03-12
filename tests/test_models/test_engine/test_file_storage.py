#!/usr/bin/python3
"""Unitest module"""

import json
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class Test_Amenity(unittest.TestCase):
    """Defines FileStorage class test cases"""
    
    def test_type(self):
        self.assertIsInstance(storage.all(), dict)
    
    def test_newobj(self):
        my_model = BaseModel()        
        name = my_model.__class__.__name__
        key = name + '.' + my_model.id
        l_obj = storage.all()
        
        self.assertEqual(l_obj[key], my_model) 
        

if __name__ == '__main__':
    unittest.main()

