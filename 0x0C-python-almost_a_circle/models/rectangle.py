#!/usr/bin/python3
"""This module holds the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """to string method"""
        out = "[Rectangle] ({}) {}/{} - {}/{}"
        return out.format(self.id, self.x, self.y, self.width, self.height)

    def to_dictionary(self):
        """returns a dictionary filled with the attributes of a Rectangle"""
        out = {
            "width": self.width, "height": self.height,
            "x": self.x, "y": self.y, "id": self.id
        }
        return out

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculated area field"""
        return self.width * self.height

    def display(self):
        """prints a visial representation of the rectangle to stdout"""
        out = " " * self.x + "#" * self.width + "\n"
        out *= self.height
        out = "\n" * self.y + out
        print(out, end="")
        return out

    def update(self, *args, **kwargs):
        """updates attribute values"""
        if args is None or args == ():
            for k, v in kwargs.items():
                setattr(self, k, v)
            return
        a = len(args)
        if a > 0:
            self.id = args[0]
        if a > 1:
            self.width = args[1]
        if a > 2:
            self.height = args[2]
        if a > 3:
            self.x = args[3]
        if a > 4:
            self.y = args[4]
