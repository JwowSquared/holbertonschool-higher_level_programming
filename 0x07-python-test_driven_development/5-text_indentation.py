#!/usr/bin/python3
"""This module holds the function text_indentation, for Python 0x07 Task 4"""


def text_indentation(text):
    """prints the given text with aditional newlines after punctuation"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for c in text:
        if c in ['.', '?', ':']:
            print("{}\n".format(c))
        else:
            print(c, end="")
