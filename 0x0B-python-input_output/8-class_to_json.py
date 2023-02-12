#!/usr/bin/python3
"""Class to JSON: """


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    for JSON serialization of an object.
    Args:
        obj (obj): An instance of a Class.
    """
    return obj.__dict__
