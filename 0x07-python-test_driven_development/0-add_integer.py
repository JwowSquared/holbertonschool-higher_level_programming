#!/usr/bin/python3
"""This module holds the function add_integer, for Python 0x07 Task 0"""


def add_integer(a, b=98):
    """adds 2 numbers, default rval of 98. converts floats to integers"""
    if type(a) not in [int, float]:
        raise TypeError("a must be integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be integer")
    return int(a) + int(b)
