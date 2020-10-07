#!/usr/bin/python3
"""x"""


def append_write(filename="", text=""):
    """x"""
    with open(filename, "a") as f:
        total = f.write(str(text))
    return total
