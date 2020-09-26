#!/usr/bin/python3
"""This module holds the function matrix_divided, for Python 0x07 Task 1"""


def matrix_divided(matrix, div):
    """returns new matrix based on old matrix with each term over div"""
    long_err = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list or type(matrix[0]) is not list:
        raise TypeError(long_err)

    for row in matrix:
        if type(row) is not list:
            raise TypeError(long_err)
        for i in row:
            if type(i) not in [int, float]:
               raise TypeError(long_err)

    cols = len(matrix[0])
    for row in matrix:
        if len(row) != cols:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    try:
        return [[round(x / div, 2) for x in list] for list in matrix]
    except:
        raise
