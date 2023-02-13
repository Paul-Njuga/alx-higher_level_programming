#!/usr/bin/python3
"""Student to JSON: """


class Student:
    """Defines a student."""
    def __init__(self, first_name, last_name, age):
        """Initializes Student class.
        Arg:
            first_name (str): Student first name.
            last_name (str): Student last name.
            age (int): Student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.
        Args:
            attrs (:obj: list of `str`, optional): List of attribute names.
        """
        rep = self.__dict__
        d = dict()
        if type(attrs) is list and all(type(k) is str for k in attrs):
            for k in attrs:
                if k in rep:
                    d.update({k: rep[k]})
            return d
        return rep
