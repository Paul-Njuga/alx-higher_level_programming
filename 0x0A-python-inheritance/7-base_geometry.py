#!/usr/bin/python3
"""Integer validator: """


class BaseGeometry:
    """Class with public instance methods."""

    def area(self):
        """
        Raises:
            Exception: If area() is not implemented.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates value."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
