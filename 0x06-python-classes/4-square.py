#!/usr/bin/python3
"""Access & update private attribute: """


class Square:
    """
    Defines a Square.
    Private instance attribute: size
        - property def size(self)
        - property setter def size(self, value)
    Instantiation with optional size
    Public instance method: def area(self)
    """
    def __init__(self, size=0):
        """
        Args:
            private optional size (int): Size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Size getter method."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
