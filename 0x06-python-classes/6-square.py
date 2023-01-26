#!/usr/bin/python3
"""Square coordinates: """


class Square:
    """
    Defines a Square.
    Private instance attribute: size.
        - property def size(self).
        - property setter def size(self, value).
    Private instance attribute: position.
        - property def position(self).
        - property setter def position(self, value).
    Instantiation with optional size & optional position.
    Public instance method: def area(self).
    Public instance method: def my_print(self).
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            private optional size (int): Size of the square.
            private optional position (int): Square coorinates.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Position getter method."""
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            return
        if self.__position[1] > 0:
            print()  #: Newline
        for i in range(size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for k in range(size):
                print("#", end="")
            print()
