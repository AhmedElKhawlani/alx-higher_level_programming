#!/usr/bin/python3
# 5-square.py by EL KHAWLANI Ahmed
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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        """
        Shows the square
        """

        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print('#', end='')
                print()
