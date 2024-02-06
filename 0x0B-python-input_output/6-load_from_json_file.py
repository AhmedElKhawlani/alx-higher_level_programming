#!/usr/bin/python3
"""
Module that defines a function that that creates an Object from a “JSON file”.
"""


def load_from_json_file(filename):
    """
    Function that that creates an Object from a “JSON file”.
    """

    import json
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
