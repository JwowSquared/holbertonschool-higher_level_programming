#!/usr/bin/python3
"""x"""


def read_lines(filename="", nb_lines=0):
    """x"""
    with open(filename, "r") as f:
        if nb_lines <= 0:
            for line in f:
                print(line, end="")
        else:
            for line in f:
                if nb_lines <= 0:
                    break
                print(line, end="")
                nb_lines -= 1
