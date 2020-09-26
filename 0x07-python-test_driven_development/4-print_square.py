#!/usr/bin/python3
"""This module holds the function print_square, for Python 0x07 Task 3"""


def print_square(size):
    """prints a square of #'s based on input size"""
    if type(size) not in [int, float]:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    try:
        for i in range(size):
            print("#" * size)
    except:
        raise
