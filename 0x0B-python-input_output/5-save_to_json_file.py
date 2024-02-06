#!/usr/bin/python3
"""
Module that defines a function that writes an Object to a text file,
using a JSON representation.
"""


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text file,
    using a JSON representation.
    """

    import json
    with open(filename, 'w', emcoding='utf-8') as f:
        json.dump(my_obj, f)
