#!/usr/bin/python3
"""x"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """x"""

    def __init__(self, size):
        """x"""
        super().integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """x"""
        out = "[Square] " + str(self._Rectangle__width)
        out += "/" + str(self._Rectangle__height)
        return out
