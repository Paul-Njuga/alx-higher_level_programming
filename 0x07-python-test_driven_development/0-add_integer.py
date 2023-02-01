#!/usr/bin/python3
"""Integer addition: """


def add_integer(a, b=98):
    """Adds 2 integers
    Returns:
        The addition of a and b.
    Raises:
        TypeError: If type(a) != int or float
        TypeError: If type(b) != int or float
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a + b)
