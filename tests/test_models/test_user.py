#!/usr/bin/python3
"""Unitest module"""

import json
import unittest
from models.user import User


class Test_user(unittest.TestCase):
    """Defines user class test cases"""
    def test_type(self):
        u = User()
        self.assertIsInstance(u, User)
    
    def test_args(self):
        u = User()
        self.assertEqual(u.email, "")
        self.assertEqual(u.password, "")
        self.assertEqual(u.last_name, "")
        self.assertEqual(u.first_name, "")
        
    def test_set_args(self):
        u = User()
        u.first_name = "Sara"
        u.email = "sara_193@gmail.com"
        self.assertEqual(u.first_name, "Sara")
        self.assertEqual(u.email, "sara_193@gmail.com")
        
            
        

if __name__ == '__main__':
    unittest.main()

