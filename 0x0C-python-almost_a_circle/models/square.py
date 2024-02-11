#!/usr/bin/python3
"""
Module that contains the definition of the class Square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Definition of the class Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Defines the string representation of instances of the class
        """
        xc = self.x
        yc = self.y
        w = self.width
        return "[Square] ({}) {}/{} - {}".format(self.id, xc, yc, w)

    @property
    def size(self):
        """
        Getter for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates a square
        """

        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        elif kwargs:
            for key in kwargs:
                if key == 'id':
                    self.id = kwargs['id']
                elif key == 'size':
                    self.size = kwargs['size']
                elif key == 'x':
                    self.x = kwargs['x']
                elif key == 'y':
                    self.y = kwargs['y']

    def to_dictionary(self):
        """
        Returns the dictionary representation of a rectangle
        """

        return {'id': self.id, 'size': self.width,
                'x': self.x, 'y': self.y}
