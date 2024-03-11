#!/usr/bin/python3
"""Unitest module"""

import json
import unittest
from models.base_model import BaseModel
from datetime import datetime


class Test_Base(unittest.TestCase):
    """Defines Base class test cases"""
    def test_two_uneq_ids(self):
        B1 = BaseModel()
        B2 = BaseModel()
        self.assertNotEqual(B1.id, B2.id)
        
    def test_datetime(self):
        B1 = BaseModel()
        self.assertIsInstance(B1.created_at, datetime)    

if __name__ == '__main__':
    unittest.main()

