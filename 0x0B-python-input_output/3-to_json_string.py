#!/usr/bin/python3
"""To JSON string: """
import json


def to_json_string(my_obj):
    """Convert an object to a JSON string.
    Args:
        my_obj (:obj): Object to convert.
    Returns:
        The JSON representation of an object (string).
    """
    return json.dumps(my_obj, sort_keys=True)
