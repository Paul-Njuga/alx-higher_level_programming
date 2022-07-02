#!/usr/bin/python3
# 6-max_integer_test.py
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_uniq_list(self):
        """Define uniq element list"""
        uniq_list = [7]
        self.assertEqual(max_integer(uniq_list), 7)

    def test_ordered_list(self):
        """Define ordered list"""
        ordered_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered_list), 4)
        with self.assertRaises(TypeError):
            max_integer([1, '2', 3])
        with self.assertRaises(TypeError):
            max_integer([1, [2], 3])

    def test_unordered_list(self):
        """Define unordered list"""
        unordered_list = [5, 6, 9, 20]
        self.assertEqual(max_integer(unordered_list), 20)

    def test_empty_list(self):
        """Define empty list"""
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_p_float_list(self):
        """Define postive float list"""
        p_float_list = [8.74, 2.54, 10.54, 4.77]
        self.assertEqual(max_integer(p_float_list), 10.54)
        with self.assertRaises(TypeError):
            max_integer([1, '2', 3.65])
        with self.assertRaises(TypeError):
            max_integer([1, [2.53], 3.34])

    def test_p_4_float_list(self):
        """Define postive with four decimal float list"""
        p_4_float_list = [8.74, -2.54, 10.545, 10.5458]
        self.assertEqual(max_integer(p_4_float_list), 10.5458)

    def test_n_float_list(self):
        """Define negative float list"""
        n_float_list = [8.74, -2.54, -10.54, 4.77]
        self.assertEqual(max_integer(n_float_list), 8.74)

    def test_n_2_float_list(self):
        """Define negative float list"""
        n_2_float_list = [-8.74, -2.54, -10.545, -10.5458]
        self.assertEqual(max_integer(n_2_float_list), -2.54)

    def test_int_float_list(self):
        """Define combine integer and float list"""
        int_float_list = [0.47, 4, 5.6, 6.6, 3, 10.43]
        self.assertEqual(max_integer(int_float_list), 10.43)

    def test_word_lw_list(self):
        """Define lowercase and uppercase word list"""
        word_lw_list = ["Holberton", "School", "SC"]
        self.assertEqual(max_integer(word_lw_list), "School")

    def test_word_up_list(self):
        """Define other lowercase and uppercase word list"""
        word_up_list = ["Holberton", "School", "SCHOOL"]
        self.assertEqual(max_integer(word_up_list), "School")

    def test_word_lw_num_list(self):
        """Define lowercase word with numbers list"""
        word_lw_num_list = ["Holberton", "School", "School444"]
        self.assertEqual(max_integer(word_lw_num_list), "School444")

    def test_word_up_num_list(self):
        """Define uppercase word with numbers list"""
        word_up_num_list = ["Holberton", "School", "SCHOOL444"]
        self.assertEqual(max_integer(word_up_num_list), "School")

    def test_beg_space_list(self):
        """Define begining spaces word list"""
        beg_space_list = ["Holberton", "        School", " School"]
        self.assertEqual(max_integer(beg_space_list), "Holberton")

    def test_chr_special_list(self):
        """Define word with character special list"""
        chr_special_list = ["Holberton", "        School", "!School    "]
        self.assertEqual(max_integer(chr_special_list), "Holberton")

    def test_chr_special_2_list(self):
        """Define other word with character special list"""
        chr_special_2_list = ["Holberton", "School!3? ", "School !?3    "]
        self.assertEqual(max_integer(chr_special_2_list), "School!3? ")

if __name__ == '__main__':
    unittest.main()
