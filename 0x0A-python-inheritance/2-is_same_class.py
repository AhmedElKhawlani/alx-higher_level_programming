#!/usr/bin/python3
"""
Defines a function that Checks if object is an instance of a class
"""


def is_same_class(obj, a_class):
    """
    Return True if object is an instance of
    a_class, False otherwise
    """
    return (type(obj) == a_class)
