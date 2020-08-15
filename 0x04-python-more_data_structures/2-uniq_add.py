#!/usr/bin/python3


def uniq_add(my_list=[]):
    sum = 0
    out = list(dict.fromkeys(my_list))
    for i in out:
        sum += i
    return sum
