#!/usr/bin/python3
"""
Defines Square class that inherits from
Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Squares class that inherits Rectangles.
    """

    def __init__(self, size):
        """Initialize a new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def ___str___(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
