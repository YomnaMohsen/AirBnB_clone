#!/usr/bin/python3
"""Unitest module"""

import json
import unittest
from models.review import Review


class Test_Review(unittest.TestCase):
    """Defines Review class test cases"""
    """Defines state class test cases"""
    def test_type(self):
        R = Review()
        self.assertIsInstance(R, Review)
        self.assertEqual(R, type(Review))
    
    def test_args(self):
        R1 = Review()
        self.assertEqual(R1.place_id, "")
        self.assertEqual(R1.text, "")
        self.assertEqual(R1.user_id, "")
        
    def test_set_args(self):
         R1 = Review()
         R1.user_id = "AB1"
         R1.place_id = "Hotel_g_Room01"
         self.assertEqual(R1.user_id, "AB1")
         self.assertEqual(R1.place_id, "Hotel_g_Room01")

if __name__ == '__main__':
    unittest.main()

