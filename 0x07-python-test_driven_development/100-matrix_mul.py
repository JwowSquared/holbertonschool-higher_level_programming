#!/usr/bin/python3
"""This module holds the function matrix_mul, for Python 0x07 Task 6
   A helper function empty is used within matrix_mul
"""


def empty(matrix):
    """checks if a valid matrix contains anything"""
    for row in matrix:
        if row:
            return False
    return True


def matrix_mul(m_a, m_b):
    """Multiply two matrices together for some reason"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")

    if empty(m_a):
        raise ValueError("m_a can't be empty")
    if empty(m_b):
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Actual logic starts here
    out = []
    for k in range(len(m_a)):
        row = []
        for i in range(len(m_b[0])):
            result = 0
            for j in range(len(m_b)):
                result += m_a[k][j] * m_b[j][i]
            row.append(result)
        out.append(row)
    return(out)
