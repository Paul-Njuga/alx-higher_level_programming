#!/usr/bin/python3
"""Create object from a JSON file: """
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”.
    Args:
        filename: JSON file to convert.
    Returns:
        An object (Python data structure) represented by a JSON string.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
