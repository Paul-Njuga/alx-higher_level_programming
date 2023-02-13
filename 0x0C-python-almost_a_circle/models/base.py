#!/usr/bin/python3
"""Base class: """
import os
import json


class Base:
    """Define the base of all other classes.
    Attributes:
        nb_objects (int): id count.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Args:
            id (:obj: `str`, optional): id of classes.
        """
        if id is not None and type(id) != int:
            raise TypeError("id must be an integer")
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.
        Args:
            list_dictionaries (:obj: list of 'dict'): List of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.
        Args:
            list_objs: A list of instances who inherits off Base.
        """
        if list_objs is None or list_objs == []:
            j_obj = "[]"
        else:
            j_obj = cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs])

        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding="utf-8") as f:
            return f.write(j_obj)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of `json_string`.
        Args:
            json_string: JSON string rep
        """
        l = []
        if json_string is not None or json_string != "":
            l = json.loads(json_string)
            return l
        return l

    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.
        Args:
        """
        pass
