#!/usr/bin/python3
""" File name : 0-add_integer.py
    Integers addition: function that adds 2 integers
    Prototype: def add_integer(a, b=98)
    You are not allowed to import any module
"""


def add_integer(a, b=98):
    """Return string with full name
    first_name and last_name must be strings
    Raises:
        TypeError: first_name must be a string
        TypeError: first_name must be a string
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
