#!/usr/bin/python3


def remove_char_at(str, n):
    if n < 0:
        return str
    out = ""
    for i in range(len(str)):
        if i != n:
            out += str[i]
    return out
