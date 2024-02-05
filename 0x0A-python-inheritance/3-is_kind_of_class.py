#!/usr/bin/python3
"""
Defines a function that checks if object is an instance
of a class or an inherited class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if object is an instance of a_class
    or a class that a_class inherits from.
    """
    return (isinstance(obj, a_class))
