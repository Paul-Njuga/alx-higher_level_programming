#!/usr/bin/python3
""" File name : 4-print_square.py
    Print square: function that prints a square with the character #
    Prototype: def print_square(size)
    You are not allowed to import any module
"""


def print_square(size):
    """function that prints a square with the character #
    size: numbers the character # to print
    Raises:
        TypeError: size must be an integer
        TypeError: size must be >= 0
    """

    if (not isinstance(size, int) or
            isinstance(size, float) and size < 0):
            raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        else:
            print("")
