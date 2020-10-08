#!/usr/bin/python3
"""This module holds unit tests for Project 0x0C, for the Base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """These tests are for the Base class"""
    def test_id(self):
        """Tests that the id properly increments"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        b3 = Base()
        b4 = Base()
        self.assertEqual(b4.id, 4)
        b98 = Base(98)
        self.assertEqual(b98.id, 98)
        b5 = Base()
        self.assertEqual(b5.id, 5)

    def test_dtj(self):
        """tests the dictionary to json string static method"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        d1 = r1.to_dictionary()
        s1 = Square(4, 2, 3, 10)
        d2 = s1.to_dictionary()
        j1 = Base.to_json_string([d1, d2])
        self.assertTrue(isinstance(j1, str))
        d3 = Base.from_json_string(j1)
        self.assertTrue(isinstance(d3, list))
