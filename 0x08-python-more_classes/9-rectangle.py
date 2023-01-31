#!/usr/bin/python3
"""A square is a rectangle: """


class Rectangle:
    """
    Defines a Rectangle.
    Private instance attribute: width.
    Private instance attribute: height.
    Instantiation with optional width, height & number_of_instances.
    Public instance method: def area(self).
    Public instance method: def perimeter(self).
    Static method def bigger_or_equal(rect_1, rect_2).

    Attributes:
        number_of_instances (int): Keeps count of instances.
        print_symbol (:obj:'list'): Used as symbol for string representation

    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Instantializes attributes & increases counter.

        Arg:
            width (int, optional): Rectangle width.
            height (int, optional): Rectangle height.

        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """Print the message "Bye rectangle..."
        when an instance is deleted & reduces counter"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    def __str__(self):
        """Returns an informal and nicely printable string representation
        of a Rectangle instance, filled with the '#' character."""
        rec_str = ''
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    rec_str += str(self.print_symbol)
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
        """Calculates the area of a Rectangle instance
        Returns:
            Area of the the rectangle, given by height * width
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a Rectangle instance
        Returns:
            Perimeter of the rectangle, given by 2 * (height + width)
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((2 * self.__width) + (2 * self.__height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Finds the biggest Rectangle based on the area

        Args:
            rect_1: Rectangle instance
            rect_2: Rectangle instance different from rect_1

        Returns:
            The instance with the biggest area,
            or rect_1 if both rectangles have the same area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        if rect_2.area() > rect_1.area:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Arg:
            size (int, optional): Square size.
        Returns:
            A new Rectangle instance with width == height == size
        """
        return cls(size, size)
