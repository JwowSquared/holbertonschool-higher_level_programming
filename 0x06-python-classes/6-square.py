#!/usr/bin/python3
"""This module is the final mandatory evolution of the Square Class"""


class Square:
    """Square Class with position attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """Basic Constructor"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter that forces a len 2 Tuple of positive integers"""
        flag = 0
        if type(value) is tuple:
            flag += 1
        if len(value) == 2:
            flag += 1
        if type(value[0]) is int and type(value[1]) is int:
            flag += 1
        if value[0] >= 0 and value[1] >= 0:
            flag += 1
        if flag == 4:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Return the area of the Square instance"""
        return self.__size ** 2

    def my_print(self):
        """Visualize the Square instance, with offset position"""
        if self.__size > 0:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
        else:
            print("")
