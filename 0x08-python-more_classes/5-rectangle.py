#!/usr/bin/python3
"""Detect instance deletion: """


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

    def __del__(self):
        """Print the message "Bye rectangle..."
        when an instance of Rectangle is deleted"""
        print("Bye rectangle...")

    def __str__(self):
        """Returns an informal and nicely printable string representation
        of a Rectangle instance, filled with the '#' character."""
        rec_str = ''
        if self.__width == 0 or self.__height == 0:
            return rec_str
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    rec_str += '#'
                rec_str += '\n'
            return rec_str[:-1]  #: Remove EOF newline

    def __repr__(self):
        """Return a string representation of a Rectangle instance
        that is able to recreate a new instance by using eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

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
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((2 * self.__width) + (2 * self.__height))
