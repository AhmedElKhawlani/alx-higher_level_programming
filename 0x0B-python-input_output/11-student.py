#!/usr/bin/python3
"""
Module that defines a class that represents students.
"""


class Student:
    """
    Class that represents students.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        """

        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            D = {k: getattr(self, k) for k in attrs if k in self.__dict__}
            return D
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance by json content
        """

        for key in json:
            setattr(self, key, json[key])
