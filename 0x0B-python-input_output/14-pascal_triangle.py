#!/usr/bin/python3
"""x"""


def pascal_triangle(n):
    """x"""
    if n <= 0:
        return [[]]

    out = []
    for i in range(1, n + 1):
        line = []
        p = 1
        for j in range(1, i + 1):
            line.append(p)
            p = int(p * (i - j) / j)
        out.append(line)
    return out
