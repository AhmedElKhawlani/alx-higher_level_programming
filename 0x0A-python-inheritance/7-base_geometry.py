#!/usr/bin/python3
"""
Defines the class BaseGeometry.
"""


class BaseGeometry:
    """
    Class that represents BaseGeometry.
    """

    def area(self):
        """
        Not implemented method.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates a value as an integer;
        Raises TypeError if value is not int;
        Raises ValueError if value is lower than 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
