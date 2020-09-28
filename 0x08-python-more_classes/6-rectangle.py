#!/usr/bin/python3
"""This module holds the task 6 evolution of the Rectangle class"""


class Rectangle:
    """Rectangle class with a public global variable number_of_instances"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """constructor with optional width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """returns a visual representation using # based on width and height"""
        out = ""
        if self.perimeter() > 0:
            for i in range(self.__height):
                out += ('#' * self.__width)
                if i < self.__height - 1:
                    out += '\n'
        return out

    def __repr__(self):
        """returns a representation of current rectangle that can be eval'd"""
        out = "Rectangle("
        out += str(self.__width) + ", " + str(self.__height)
        return out + ")"

    def __del__(self):
        """a heartfelt goodbye for each rectangle brother we lose"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculated area based on width and height"""
        return self.__width * self.__height

    def perimeter(self):
        """calculated perimeter based on width and height"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
