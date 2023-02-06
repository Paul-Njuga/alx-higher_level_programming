#!/usr/bin/python3
"""Same class or inherit from: """


def is_kind_of_class(obj, a_class):
    """Finds if obj is an instance of a_class or a class
    inherited from a_class.

    Args:
        obj: object to look at
        a_class: class to evaluate

    Returns:
        True or False
    """

    return isinstance(obj, a_class)
