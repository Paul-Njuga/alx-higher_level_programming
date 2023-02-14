#!/usr/bin/python3
"""Unnitest base.
Test cases for Base class.
Each test has the number of the task,
and the number of the test for that task
(i.e 'test_3_0' for the first test of task 3)
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test class for Base class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_1_0(self):
        """Create new instances: check for id."""

        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base()
        self.assertEqual(b3.id, 2)
        b4 = Base(-5)
        self.assertEqual(b4.id, -5)

    def test_1_1(self):
        """Create new instances: check for type(id) not int."""

        with self.assertRaises(TypeError):
            Base("id")
        with self.assertRaises(TypeError):
            Base([1])
        with self.assertRaises(TypeError):
            Base(2.5)

    def test_1_2(self):
        """Test for type and instance of id."""

        b1 = Base()
        self.assertEqual(type(b1), Base)
        self.assertTrue(isinstance(b1, Base))


if __name__ == '__main__':
    unittest.main()
