#!/usr/bin/python3
"""Simple rectangle: """


class Rectangle:
    """
    Defines a Rectangle.
    Private instance attribute: width.
    Private instance attribute: height.
    Instantiation with optional width and height.
    """
    def __init__(self, width=0, height=0):
        """Instantializes attributes.

        Arg:
            width (int, optional): Rectangle width.
            height (int, optional): Rectangle height.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Returns width."""
        return self.__width

    @property
    def height(self):
        """Returns height."""
        return self.__height

    @width.setter
    def width(self, val):
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        elif val < 0:
            raise ValueError("width must be >= 0")
        else:
            return self.__width

    @height.setter
    def height(self, val):
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        elif val < 0:
            raise ValueError("height must be >= 0")
        else:
            return self.__height
