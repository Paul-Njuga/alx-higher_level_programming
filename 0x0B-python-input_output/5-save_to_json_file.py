#!/usr/bin/python3
"""Save Object to a file: """
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation.
    Args:
        my_obj (:obj): Object to convert to JSON.
        filename: File to write to.
    """
    with open(filename, 'w', encoding="utf-8"):
        json.dump(my_obj, filename)
