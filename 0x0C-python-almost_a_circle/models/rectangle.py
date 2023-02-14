#!/usr/bin/python3
"""First Rectangle: """
from models.base import Base


class Rectangle(Base):
    """Defines class Rectangle that inherits from Base."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance.
        Args:
            private width (int): Width.
            private height (int): Height.
            private optional x (int): x.
            private optional y (int): y.
            private optional id (int): id.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width getter method."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height getter method."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter method."""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter method."""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance."""
        return (self.__width * self.__height)

    def display(self):
        """Prints in stdout the Rectangle instance with the character #."""
        for line in range(self.__y):
            print()
        for i in range(self.__height):
            for space in range(self.__x):
                print(" ", end='')
            for j in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """Returns an informal and nicely printable string representation
        of a Rectangle instance."""
        s = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.__width, self.__height)
        return s

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute.
        Args:
            *args: Variable length argument list.
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if args[0] is not None and type(args[0]) != int:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == "id":
                        if type(value) != int and value is not None:
                            raise TypeError("id must be an integer")
                        self.id = value
                    if key == "width":
                        self.__width = value
                    if key == "height":
                        self.__height = value
                    if key == "x":
                        self.__x = value
                    if key == "y":
                        self.__y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        new_dict = {'id': self.id, 'width': self.__width,
                    'height': self.__height, 'x': self.__x, 'y': self.__y}
        return new_dict
