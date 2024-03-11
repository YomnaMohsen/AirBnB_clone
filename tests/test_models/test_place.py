#!/usr/bin/python3
"""Unitest module"""

import json
import unittest
from models.place import Place


class Test_Base(unittest.TestCase):
    """Defines place class test cases"""
    """Defines user class test cases"""
    def check_type(self):
        p = Place()
        self.assertIsInstance(p, Place)

if __name__ == '__main__':
    unittest.main()

