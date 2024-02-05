#!/usr/bin/python3
"""
    This module defines a function that returns
    the list of available attributes and methods
    of an object
"""


def lookup(obj):
    """This functions returns the list of available
    attributes and methods of an object
    """
    return dir(obj)
