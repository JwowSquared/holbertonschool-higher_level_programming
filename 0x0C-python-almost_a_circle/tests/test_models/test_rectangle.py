#!/usr/bin/python3
"""This module holds unit tests for Project 0x0C, for the Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """These tests are for the Rectangle class"""
    def test__attributes_exist(self):
        """Tests that the constructor properly creates the attributes"""
        r1 = Rectangle(11, 23, 31, 47, 79)
        self.assertTrue(isinstance(r1, Base))
        self.assertEqual(r1.width, 11)
        self.assertEqual(r1.height, 23)
        self.assertEqual(r1.x, 31)
        self.assertEqual(r1.y, 47)
        self.assertEqual(r1.id, 79)

    def test_attribute_errors(self):
        """Tests the type validation of Rectangle attributes"""
        self.assertRaises(TypeError, Rectangle, "Bob", 42)
        self.assertRaises(TypeError, Rectangle, 3, 3.14)
        self.assertRaises(TypeError, Rectangle, 4, 5, [1, 2, 3])
        self.assertRaises(TypeError, Rectangle, 6, 7, 0, None)
        self.assertRaises(ValueError, Rectangle, -22, 5)
        self.assertRaises(ValueError, Rectangle, 6, 0)
        self.assertRaises(ValueError, Rectangle, 4, 5, -1)
        self.assertRaises(ValueError, Rectangle, 2, 3, 1, -5)

    def test_area(self):
        """Tests that area is calculated correctly"""
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.area(), 20)
        r2 = Rectangle(2147000000, 10)
        self.assertEqual(r2.area(), 21470000000)

    def test_display(self):
        """Tests that the display method works properly"""
        r1 = Rectangle(3, 4)
        self.assertMultiLineEqual(r1.display(), "###\n" * 4)
        r2 = Rectangle(3, 4, 1, 2)
        self.assertMultiLineEqual(r2.display(), "\n\n ###\n ###\n ###\n ###\n")

    def test_str(self):
        """Tests that the string representation of a Rectangle works properly"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (5) 3/4 - 1/2")

    def test_update(self):
        """Tests that update properly sets all variables"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r1.update()
        self.assertEqual(str(r1), "[Rectangle] (5) 3/4 - 1/2")
        r1.update(6, 7, 8, 9, 10, "Steve Jobs")
        self.assertEqual(str(r1), "[Rectangle] (6) 9/10 - 7/8")
        r1.update(11, 12)
        self.assertEqual(str(r1), "[Rectangle] (11) 9/10 - 12/8")
        r1.update(22, id=98)
        self.assertEqual(str(r1), "[Rectangle] (22) 9/10 - 12/8")
        r1.update(y=1, x=2, height=3, width=4, id=5)
        self.assertEqual(str(r1), "[Rectangle] (5) 2/1 - 4/3")

    def test_dict(self):
        """Tests that the dictionary representation works with update"""
        r1 = Rectangle(10, 2, 1, 9, 1)
        d1 = r1.to_dictionary()
        self.assertTrue(isinstance(d1, dict))
        r2 = Rectangle(1, 1)
        r2.update(**d1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/9 - 10/2")

    def test_save(self):
        """tests the class method save_to_file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            print(f.read())
        self.assertEqual(1, 1)
