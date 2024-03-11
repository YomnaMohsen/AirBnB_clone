#!/usr/bin/python3
"""Unitest module"""

import json
import unittest
from models.place import Place


class Test_place(unittest.TestCase):
    """Defines place class test cases"""
    def check_type(self):
        p = Place()
        self.assertIsInstance(p, Place)
        
    def test_args(self):
        p = Place()
        self.assertEqual(p.name, "")
        self.assertEqual(p.latitude, 0.0)
        self.assertEqual(p.max_guest, 0)
        self.assertIsInstance(p.amenity_ids, list)
        
    def test_set_args(self):
         p = Place()
         p.name = "garden hotel"
         self.assertEqual(p.name, "garden hotel")
         p.max_guest += 2
         self.assertEqual(p.max_guest, 2)  
    
        
            
if __name__ == '__main__':
    unittest.main()

