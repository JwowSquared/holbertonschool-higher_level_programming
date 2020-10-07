#!/usr/bin/python3
"""x"""


class BaseGeometry:
    """x"""
    def area(self):
        """x"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """x"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
