#!/usr/bin/python3
"""
Module that contains the definition of the class Base
"""


import json
import csv
import turtle


class Base:
    """
    Definition of class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializing a Base instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries
        """

        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        """
        file = cls.__name__ + ".json"
        with open(file, "w", encoding="utf-8") as f:
            if not list_objs:
                f.write("[]")
            else:
                dicts = [x.to_dictionary() for x in list_objs]
                f.write(cls.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        """
        if dictionary:
            if cls.__name__ == 'Square':
                dummy = cls(7)
            else:
                dummy = cls(12, 6)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a json file
        """
        name = cls.__name__
        file = name + ".json"
        try:
            with open(file, 'r', encoding='utf-8') as f:
                data = f.read()
        except IOError:
            return []
        data = Base.from_json_string(data)
        return [cls.create(**dict_obj) for dict_obj in data]
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Writes list_objs to a csv file
        """

        file = cls.__name__ + ".csv"
        with open(file, "w", newline="") as f:
            if not list_objs:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    header = ["id", "width", "height", "x", "y"]
                else:
                    header = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=header)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Loads objects from a csv file
        """

        file = cls.__name__ + ".csv"
        try:
            with open(file, "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    header = ["id", "width", "height", "x", "y"]
                else:
                    header = ["id", "size", "x", "y"]
                dicts = csv.DictReader(f, fieldnames=header)
                dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in dicts]
                return [cls.create(**d) for d in dicts]
        except IOError:
            return []
    
    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw Rectangles and Squares using the turtle module
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rectangle in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rectangle.x, rectangle.y)
            turt.down()
            for i in range(2):
                turt.forward(rectangle.width)
                turt.left(90)
                turt.forward(rectangle.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for square in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(square.x, square.y)
            turt.down()
            for i in range(2):
                turt.forward(square.width)
                turt.left(90)
                turt.forward(square.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
