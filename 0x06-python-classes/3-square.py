#!/usr/bin/python3
# 3-square.py by EL KHAWLANI Ahmed
"""Define a class that represents squares"""


class Square:
    """ Class that represents squares"""

    def __init__(self, size=0):
        """Initializing a square
        Args: - size: size of the square
        Raises:
            TypeError: if size is not integer
            ValueError: if size is negative
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Calculate area of the square
        Returns: The area of the square
        """

        return (self.__size ** 2)
