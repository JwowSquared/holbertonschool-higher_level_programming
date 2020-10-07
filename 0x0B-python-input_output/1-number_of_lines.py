#!/usr/bin/python3
"""x"""


def number_of_lines(filename=""):
    """x"""
    with open(filename, "r") as f:
        total = len(f.readlines())
    return total
