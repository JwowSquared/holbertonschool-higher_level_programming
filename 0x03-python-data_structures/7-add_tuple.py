#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    out = [0, 0]
    for i in range(2):
        if len_a > i:
            out[i] += tuple_a[i]
        if len_b > i:
            out[i] += tuple_b[i]
    return (out[0], out[1])
