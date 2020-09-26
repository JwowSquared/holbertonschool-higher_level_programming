#!/usr/bin/python3
"""This module holds the function lazy_matrix_mul, for Python 0x07 Task 7"""


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices together with numpy"""
    try:
        import numpy
        ma = numpy.array(m_a)
        mb = numpy.array(m_b)
        return numpy.matmul(ma, mb)
    except:
        raise
