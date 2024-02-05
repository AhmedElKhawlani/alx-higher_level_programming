#!/usr/bin/python3
"""
Defines a function that checks if an object is an instance of a class
that inherited from another class or not.
"""


def inherits_from(obj, a_class):
    """
    Returns True if object is an instance of a class that inherited
    from a_class, False otherwise.
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
