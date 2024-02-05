#!/usr/bin/python3
"""
    This module defines a class that inherits from list
"""


class MyList(list):
    """
    This class inherits from list
    """
    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort)
        """
        new = sorted(self)
        print(new)
