#!/usr/bin/python3
"""
Module that contains the definition of the class Rectangle
"""


from models.base import Base


class Rectangle(Base):
    """
    Definition of the class Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializing a Rectangle instance
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @property
    def x(self):
        """
        x getter
        """
        return self.__x

    @property
    def y(self):
        """
        y getter
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        height setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """
        x setter
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """
        y setter
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Computes the area of a rectangle
        """
        return self.__height * self.__width

    def display(self):
        """
        Displays the rectangle using #
        """

        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Defines the string representation of instances of the class
        """
        xc = self.__x
        yc = self.__y
        w = self.__width
        h = self.__height
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, xc, yc, w, h)

    def update(self, *args, **kwargs):
        """
        Updates a rectangle
        """

        if args:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        elif kwargs:
            for key in kwargs:
                if key == 'id':
                    self.id = kwargs['id']
                elif key == 'width':
                    self.width = kwargs['width']
                elif key == 'height':
                    self.height = kwargs['height']
                elif key == 'x':
                    self.x = kwargs['x']
                elif key == 'y':
                    self.y = kwargs['y']

    def to_dictionary(self):
        """
        Returns the dictionary representation of a rectangle
        """

        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
