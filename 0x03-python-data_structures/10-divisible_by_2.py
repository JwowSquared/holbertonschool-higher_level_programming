#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    if my_list is None or my_list == []:
        return None
    out = []
    for i in my_list:
        if i % 2 == 0:
            out.append(True)
        else:
            out.append(False)
    return out
