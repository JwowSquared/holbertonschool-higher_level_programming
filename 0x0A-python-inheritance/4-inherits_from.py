#!/usr/bin/python3
"""x"""


def inherits_from(obj, a_class):
    """x"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
