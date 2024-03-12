#!/usr/bin/python3
"""Unitest module"""

import json
import unittest
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    """Defines Amentiy class test cases"""
    def test_type(self):
        A1 = Amenity()
        self.assertIsInstance(A1, Amenity)
    
    def test_args(self):
        A2 = Amenity()
        self.assertEqual(A2.name, "")
        
    def test_set_args(self):
         A3 = Amenity()
         A3.name = "Wifi"
         self.assertEqual(A3.name, "Wifi")
        
            
    

if __name__ == '__main__':
    unittest.main()

