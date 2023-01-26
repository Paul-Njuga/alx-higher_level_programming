#!/usr/bin/python3
"""Square Area: """


class Square:
    """
    Defines a Square.
    Private instance attribute: size
    Instantiation with optional size
    Public instance method: def area(self)
    """
    def __init__(self, size=0):
        """
        Args:
            private optional size (int): Size of the square.
        
        Raises:
            TypeError: If type(size) != int.
            ValueError: If 'size' < 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns area of the square."""
        return self.__size ** 2
