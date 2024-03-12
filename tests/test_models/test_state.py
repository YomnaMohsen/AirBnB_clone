#!/usr/bin/python3
"""Unitest module"""

import json
import unittest
from models.state import State


class Test_state(unittest.TestCase):
    """Defines state class test cases"""
    def test_type(self):
        s = State()
        self.assertIsInstance(s, State)
    
    def test_args(self):
        s1 = State()
        self.assertEqual(s1.name, "")
        
    def test_set_args(self):
         s1 = State()
         s1.name = "morroco"
         self.assertEqual(s1.name, "morroco")
        
            

if __name__ == '__main__':
    unittest.main()
