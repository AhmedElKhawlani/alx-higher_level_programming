#!/usr/bin/python3
"""
Defines Rectangle class that inherits from
BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangles class that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Intialize a new Rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of a rectangle.
        """
        return self.__width * self.__height

    def ___str___(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
