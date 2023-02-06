#!/usr/bin/python3
"""Improve Geometry: """


class BaseGeometry:
    """Class with public instance method."""

    def area(self):
        """
        Raises:
            Exception: If the area() is not implemented.
        """
        raise Exception('area() is not implemented')
