#!/usr/bin/python3
# 7-rectangle.py by EL KHAWLANI Ahmed
""" Defines a class that represents rectangles"""


class Rectangle:
    """ Class that represents rectangles """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns The area of a rectangle"""

        return self.height * self.width

    def perimeter(self):
        """ Returns the perimeter of a rectangle"""

        if self.width * self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        if self.width * self.height == 0:
            return ''
        ch = ''
        for i in range(self.height):
            ch = ch + self.width * str(self.print_symbol) + '\n'
        return ch[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
