#!/usr/bin/python3
"""This module holds the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of a square"""
        out = "[Square] ({}) {}/{} - {}"
        return out.format(self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """returns a dictionary filled with the attributes of a Square"""
        out = {"size": self.size, "x": self.x, "y": self.y, "id": self.id}
        return out

    @property
    def size(self):
        """getter"""
        return self.width

    @size.setter
    def size(self, value):
        """setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates attribute values of a square"""
        if args is None or args == ():
            for k, v in kwargs.items():
                setattr(self, k, v)
            return
        a = len(args)
        if a > 0:
            self.id = args[0]
        if a > 1:
            self.size = args[1]
        if a > 2:
            self.x = args[2]
        if a > 3:
            self.y = args[3]
