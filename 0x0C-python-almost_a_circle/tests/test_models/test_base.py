#!/usr/bin/python3
"""
This module defines unittests for base.py

Index:
    Testing __init__() - line 20
    Testing to_json_string() - line 
    Testing save_to_file() - line 
    Testing from_json_string() - line 
    Testing create() - line 
    Testing load_from_file() - line 
    Testing save_to_file_csv() - line 
    Testing load_from_file_csv() - line 
"""

import unittest
from models.base import Base


class test_base_init(unittest.TestCase):
    """
    Testing __init__() for the class Base
    """

    def test_with_arg(self):
        base = Base(15)
        self.assertEqual(15, base.id)
    
    def test_without_arg(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id + 1, base2.id)
    
    def test_None_arg(self):
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id + 1, base2.id)
    
    def test_other_type_arg(self):
        base = Base('A')
        self.assertEqual(base.id, 'A')

if __name__ == "__main__":
    unittest.main()