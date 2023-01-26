#!/usr/bin/python3
"""Printing a square: """


class Square:
    """
    Defines a Square.
    Private instance attribute: size.
        - property def size(self).
        - property setter def size(self, value).
    Instantiation with optional size.
    Public instance method: def area(self).
    Public instance method: def my_print(self).
    """
    def __init__(self, size=0):
        """
        Args:
            private optional size (int): Size of the square.
        """
        self.size = size

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

    def my_print(self):
        """
        Prints in stdout the square with the character #.
        """
        size = self.__size
        if size == 0:
            print()  #: Newline
        else:
            for i in range(size):
                for j in range(size):
                    print("#", end="")
                print()  #: Newline
