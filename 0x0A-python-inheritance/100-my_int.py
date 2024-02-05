#!/usr/bin/python3
"""
Defines a class that inherits from int
The class is inversing the equality.
"""


class MyInt(int):
    """
    a Class that inherits from int;
    thos class ir rebeling.
    """

    def __eq__(self, other):
        return self.real != other

    def __ne__(self, other):
        return self.real == other
