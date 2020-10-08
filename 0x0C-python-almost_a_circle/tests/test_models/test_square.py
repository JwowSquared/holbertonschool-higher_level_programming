#!/usr/bin/python3
"""This module holds unit tests for Project 0x0C, for the Square class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """These tests are for the Square class"""
    def test__attributes_exist(self):
        """Tests that the constructor properly creates the attributes"""
        s1 = Square(11, 31, 47, 79)
        self.assertTrue(isinstance(s1, Base))
        self.assertTrue(isinstance(s1, Rectangle))
        self.assertEqual(s1.width, 11)
        self.assertEqual(s1.height, 11)
        self.assertEqual(s1.x, 31)
        self.assertEqual(s1.y, 47)
        self.assertEqual(s1.id, 79)

    def test_attribute_errors(self):
        """Tests the type validation of Square attributes"""
        self.assertRaises(TypeError, Square, "Bob")
        self.assertRaises(TypeError, Square, 3.14)
        self.assertRaises(TypeError, Square, 4, [1, 2, 3])
        self.assertRaises(TypeError, Square, 6, 0, None)
        self.assertRaises(ValueError, Square, -22)
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, 4, -1)
        self.assertRaises(ValueError, Square, 2, 1, -5)

    def test_area(self):
        """Tests that area is calculated correctly"""
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

    def test_display(self):
        """Tests that the display method works properly"""
        s1 = Square(4)
        self.assertMultiLineEqual(s1.display(), "####\n" * 4)
        s2 = Square(4, 1, 2)
        self.assertMultiLineEqual(s2.display(), "\n\n ####\n ####\n ####\n ####\n")

    def test_str(self):
        """Tests that the string representation of a Square works properly"""
        s1 = Square(1, 3, 4, 5)
        self.assertEqual(str(s1), "[Square] (5) 3/4 - 1")

    def test_update(self):
        """Tests that update properly sets all variables"""
        s1 = Square(1, 3, 4, 5)
        s1.update()
        self.assertEqual(str(s1), "[Square] (5) 3/4 - 1")
        s1.update(6, 8, 9, 10, "Steve Jobs")
        self.assertEqual(str(s1), "[Square] (6) 9/10 - 8")
        s1.update(11, 12)
        self.assertEqual(str(s1), "[Square] (11) 9/10 - 12")
        s1.update(22, id=98)
        self.assertEqual(str(s1), "[Square] (22) 9/10 - 12")
        s1.update(y=1, x=2, size=3, id=5)
        self.assertEqual(str(s1), "[Square] (5) 2/1 - 3")

    def test_dict(self):
        """Tests that the dictionary representation works with update"""
        s1 = Square(10, 1, 9, 1)
        d1 = s1.to_dictionary()
        self.assertTrue(isinstance(d1, dict))
        s2 = Square(1)
        s2.update(**d1)
        self.assertEqual(str(s2), "[Square] (1) 1/9 - 10")
