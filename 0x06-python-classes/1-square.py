#!/usr/bin/python3

"""Defines a Square."""


class Square:
    """
    Private instance attribute: size
    Instantiation with size (no type/value verification)
    """

    def __init__(self, size):
        """
        Args:
            private size (int): Size of the square.
        """
        self.__size = size
