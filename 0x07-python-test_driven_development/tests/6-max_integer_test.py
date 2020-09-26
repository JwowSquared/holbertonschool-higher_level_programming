#!/usr/bin/python3
"""This module holds unit tests for the max_integer function"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """These tests are for the function max_integer"""
    def test_max(self):
        """Basic Use Cases"""
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([9, 1, 1]), 9)
        self.assertEqual(max_integer([2, 4, 2]), 4)
        self.assertEqual(max_integer([4, -8, 6, 0]), 6)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([12]), 12)
        self.assertIsNone(max_integer())
