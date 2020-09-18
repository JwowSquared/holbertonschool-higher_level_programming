#!/usr/bin/python3
"""This module is an evolution of the Square Class"""


class Square:
    """Square Class with area method"""
    def __init__(self, size=0):
        """Constructor that forces positive integer into size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the Square instance"""
        return self.__size ** 2
