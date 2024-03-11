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
        
    def check_args(self):
        p = Place()
        self.assertEqual(p.description, "")
        self.assertEqual(p.city_id, "")
        self.assertEqual(p.latitude, 0.0)
        self.assertIsInstance(p.name, str)
            

if __name__ == '__main__':
    unittest.main()

