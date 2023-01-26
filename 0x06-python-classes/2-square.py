#!/usr/bin/python3

"""Size Validation: """


class Square:
    """
    Defines a Square
    Private instance attribute: size
    Instantiation with optional size
    """
    def __init__(self, size=0):
        """
        Args:
            private optional size (int): Size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
