#!/usr/bin/python3
""" Print square: """


def print_square(size):
    """Function that prints a square with the character #.
    Args:
        size (int): Number of the character # to print.
    Raises:
        TypeError: size must be an integer
        TypeError: size must be >= 0
    """

    if (not isinstance(size, int) or (isinstance(size, float) and size < 0)):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        else:
            print()  #: Newline
