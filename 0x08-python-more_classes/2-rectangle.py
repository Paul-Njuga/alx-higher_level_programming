#!/usr/bin/python3
"""Area and Perimeter: """


class Rectangle:
    """
    Defines a Rectangle.
    Private instance attribute: width.
    Private instance attribute: height.
    Instantiation with optional width and height.
    Public instance method: def area(self)
    Public instance method: def perimeter(self)
    """
    def __init__(self, width=0, height=0):
        """Instantializes attributes.

        Arg:
            width (int, optional): Rectangle width.
            height (int, optional): Rectangle height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns rectangle width."""
        return self.__width

    @property
    def height(self):
        """Returns rectangle height."""
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area."""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((2 * self.__width) + (2 * self.__height))
