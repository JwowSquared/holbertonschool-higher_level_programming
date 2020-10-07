#!/usr/bin/python3
"""x"""


def write_file(filename="", text=""):
    """x"""
    with open(filename, "w") as f:
        total = f.write(str(text))
    return total
