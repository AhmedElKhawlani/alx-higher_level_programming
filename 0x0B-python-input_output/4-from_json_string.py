#!/usr/bin/python3
"""
Module that defines a function that returns an
object (Python data structure) represented by a JSON string.
"""


def from_json_string(my_str):
    """
    Function that returns an object (Python data structure)
    represented by a JSON string.
    """

    import json
    return json.loads(my_str)
