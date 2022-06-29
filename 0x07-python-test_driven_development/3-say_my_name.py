#!/usr/bin/python3
# 3-say_my_name.py
""" File name : 3-say_my_name.py
    Say my name: function that prints My name is <first name> <last name>
    Prototype: def say_my_name(first_name, last_name="")
    You are not allowed to import any module
"""


def say_my_name(first_name, last_name=""):
    """Return string with full name
    first_name and last_name must be strings
    Raises:
        TypeError: first_name must be a string
        TypeError: first_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
