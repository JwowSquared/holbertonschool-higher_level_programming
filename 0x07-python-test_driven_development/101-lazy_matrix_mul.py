#!/usr/bin/python3
"""This module holds the function lazy_matrix_mul, for Python 0x07 Task 7"""


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices together with numpy"""
    try:
        import numpy
        if type(m_a) is not list:
            raise TypeError("m_a must be a list")
        if type(m_b) is not list:
            raise TypeError("m_b must be a list")
        ma = numpy.array(m_a)
        mb = numpy.array(m_b)
        return numpy.array2string(numpy.dot(ma, mb))
    except:
        raise
