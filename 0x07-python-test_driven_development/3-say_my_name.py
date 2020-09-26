#!/usr/bin/python3
"""This module holds the function say_my_name, for Python 0x07 Task 2"""


def say_my_name(first_name, last_name=""):
    """prints a short sentence based on input"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
