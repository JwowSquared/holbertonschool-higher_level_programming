#!/usr/bin/python3
"""x"""


def read_file(filename=""):
    """x"""
    with open(filename, "r") as f:
        for line in f:
            print(line, end="")
