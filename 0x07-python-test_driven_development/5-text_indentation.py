#!/usr/bin/python3
"""This module holds the function text_indentation, for Python 0x07 Task 4"""


def text_indentation(text):
    """prints the given text with aditional newlines after punctuation"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    line = ""
    for c in text:
        line += c
        if c in ['.', '?', ':']:
            print("{}\n".format(line.strip()))
            line = ""
    print(line.strip(), end="")
