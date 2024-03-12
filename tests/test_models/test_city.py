#!/usr/bin/python3
"""Unitest module"""

import json
import unittest
from models.city import City


class Test_City(unittest.TestCase):
    """Defines City class test cases"""
    def test_type(self):
        C = City()
        self.assertIsInstance(C, City)
    
    def test_args(self):
        C1 = City()
        self.assertEqual(C1.name, "")
        self.assertEqual(C1.state_id, "")
        
    def test_set_args(self):
         C2 = City()
         C2.name = "Luxor"
         self.assertEqual(C2.name, "Luxor")
        
            

if __name__ == '__main__':
    unittest.main()

