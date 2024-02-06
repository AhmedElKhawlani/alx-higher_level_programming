#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then save them to a file.
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    L = load_from_json_file("add_item.json")
except FileNotFoundError:
    L = []
arg = sys.argv
for x in arg[1:]:
    L.append(x)
save_to_json_file(L, "add_item.json")
