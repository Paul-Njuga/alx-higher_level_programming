#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([...])."""

    def test_regular(self):
        """Test with a regular list of ints: should return the max result"""
        max_end_list = [1, 2, 3]  #: Ordered list
        max_middle_list = [1, 3, 2]  #: Unordered list
        max_begin_list = [3, 2, 1] #: Reversed list
        self.assertEqual(max_integer(max_end_list), 3)
        self.assertEqual(max_integer(max_middle_list), 3)
        self.assertEqual(max_integer(max_begin_list), 3)

    def test_unique(self):
        """Test with a list of one int: should return the value of this int"""
        uniq_list = [1]
        self.assertEqual(max_integer(uniq_list), 1)

    def test_identical(self):
        """Test with a list of identical values: should return the value"""
        dup_list = [7, 7, 7, 7, 7, 7, 7]
        self.assertEqual(max_integer(dup_list), 7)

    def test_negative(self):
        """Test with a list of negative ints: should return the max result"""
        mixed_list = [1, -2, 3]  #: Mixed types
        neg_list = [-1, -2, -3]  #: Same type
        self.assertEqual(max_integer(mixed_list), 3)
        self.assertEqual(max_integer(neg_list), -1)

    def test_float(self):
        """Test with a list of mixed ints and floats: should return the max"""
        float_list = [1, 2, 3.0]
        self.assertEqual(max_integer(float_list), 3.0)

    def test_empty(self):
        """Test with an empty list: should return None"""
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_not_int(self):
        """Test with a list of non-ints and ints: should raise a TypeError exception"""
        with self.assertRaises(TypeError):
            max_integer([1, '2', 3])

    def test_not_list(self):
        """Test with a parameter that's not a list: should raise a TypeError"""
        with self.assertRaises(TypeError):
            max_integer(7)

    def test_strings(self):
        """Test with a list of strings: should return the first string"""
        word_list = ["Hi", "World"]
        self.assertEqual(max_integer(word_list), "World")

    def test_beg_space_list(self):
        """Test with a list of strings with space: should return the string without or with less spaces"""
        word_space_list = ["Hi     ", "World"]
        self.assertEqual(max_integer(word_space_list), "World")

    def test_none(self):
        """Test with a None as parameter: should raise a TypeError"""
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == '__main__':
    unittest.main()
