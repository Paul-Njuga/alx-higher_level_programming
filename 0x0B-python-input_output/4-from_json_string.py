#!/usr/bin/python3
"""To JSON string: """
import json


def from_json_string(my_str):
    """Converts JSON string to Object.
    Args:
        my_str (:obj): JSON string representation.
    Returns:
        An object (Python data structure) represented by a JSON string.
    """
    return json.loads(my_str)
