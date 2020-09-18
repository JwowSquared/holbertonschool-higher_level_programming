#!/usr/bin/python3
"""This module is an evolution of the Square Class"""


class Square:
    """Square Class with print method"""
    def __init__(self, size=0):
        """Basic Constructor"""
        self.size = size

    @property
    def size(self):
        """Getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter that forces a positive integer"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the Square instance"""
        return self.__size ** 2

    def my_print(self):
        """Visualize the Square instance"""
        if self.__size > 0:
            for i in range(self.__size):
                print("#" * self.__size)
        else:
            print("")
