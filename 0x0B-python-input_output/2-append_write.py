#!/usr/bin/python3
"""
Module that defines a function that appends in a text file (UTF8).
"""


def append_write(filename="", text=""):
    """
    Function that appends a string to a text file (UTF8) and
    returns the number of characters written.
    """

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
