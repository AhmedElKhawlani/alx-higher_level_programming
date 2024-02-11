#!/usr/bin/python3
"""
Module that contains the definition of the class Base
"""


import json


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
