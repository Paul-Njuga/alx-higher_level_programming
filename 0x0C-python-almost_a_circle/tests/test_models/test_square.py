#!/usr/bin/python3
"""Unnitest square.
Test cases for Square class.
Each test has the number of the task,
and the number of the test for that task
(i.e 'test_3_0' for the first test of task 3)
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test class for Square class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_10_0(self):
        """Test Square class: check for attribute values."""

        s1 = Square(1)
        self.assertEqual(s1.id, 1)

        s2 = Square(10, 20, 30)
        self.assertEqual(s2.width, 10)
        self.assertEqual(s2.height, 10)
        self.assertEqual(s2.x, 20)
        self.assertEqual(s2.y, 30)
        self.assertEqual(s1.id, 2)

    def test_10_1(self):
        """Test Rectangle class: check for inheritance."""

        s1 = Square(1, 2)
        self.assertTrue(isinstance(s1, Rectangle))
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertFalse(isinstance(Square, Rectangle))
        self.assertTrue(isinstance(s1, Base))
        self.assertTrue(issubclass(Square, Base))
        self.assertFalse(isinstance(Square, Base))

    def test_10_2(self):
        """Test __str__ representation."""

        s1 = Square(10, 9, 8, 7)
        self.assertEqual(str(s1), "[Square] (7) 9/8 - 10")

    def test_10_3(self):
        """Test Square for methods inherited from Rectangle."""

        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

        s2 = Square(4, 1, 2, 5)
        s2.update(7)
        self.assertEqual(s2.id, 7)

    def test_11_0(self):
        """Test Square class: check for size attribute."""

        s1 = Square(5)
        self.assertEqual(s1.size, 8)

        s2 = Square(10, 8, 6, 4)
        self.assertEqual(s2.size, 10)

    def test_12_0(self):
        """Test update method on Square."""

        s1 = Square(5)
        s1.update(10)
        self.assertEqual(s1.id, 10)

        s1.update(x=12)
        self.assertEqual(s1.x, 12)

        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.y, 1)

    def test_14_0(self):
        """Test for public method to_dictionary."""

        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s_dictionary = {'x': 2, 'y': 1, 'id': 1, 'size': 10}
        self.assertEqual(len(s1_dictionary), len(s_dictionary))
        self.assertEqual(type(s1_dictionary), dict)

        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        s2_dictionary = s2.to_dictionary()
        self.assertEqual(len(s1_dictionary), len(s2_dictionary))
        self.assertEqual(type(s2_dictionary), dict)
        self.assertFalse(s1 == s2)


if __name__ == '__main__':
    unittest.main()
