#!/usr/bin/python3
"""The Square: """
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines class Square that inherits from Rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance.
        Args:
            size (int): value assigned to width & height.
            x (:obj: `int`, optional): x.
            y (:obj: `int`, optional): y.
            id (:obj: `int`, optional): id.
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns an informal and nicely printable string representation
        of a Square instance."""
        s = "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)
        return s

    @property
    def size(self):
        """Size getter method."""
        return self.__width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute.
        Args:
            *args: Variable length argument list.
            *kwargs: Arbitrary keyword arguments.
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if args[0] is not None and type(args[0]) != int:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == "id":
                        if type(value) != int and value is not None:
                            raise TypeError("id must be an integer")
                        self.id = value
                    if key == "size":
                        self.size = value
                    if key == "x":
                        self.x = value
                    if key == "y":
                        self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        new_dict = {'id': self.id, 'size': self.size,
                    'x': self.x, 'y': self.y}
        return new_dict
