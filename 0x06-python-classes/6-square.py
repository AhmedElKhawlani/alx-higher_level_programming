#!/usr/bin/python3
# 6 -square.py by EL KHAWLANI Ahmed
"""Define a class that represents squares"""


class Square:
    """ Class that represents squares"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing a square
        Args: - size: size of the square
        Raises:
            TypeError: if size is not integer
            ValueError: if size is negative
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if (not isinstance(value[0], int)) or (not isinstance(value[1], int)):
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        """
        Shows the square
        """

        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.position[0]):
                    print(' ', end='')
                for j in range(self.size):
                    print('#', end='')
                print()
            for i in range(self.position[1]):
                print()
