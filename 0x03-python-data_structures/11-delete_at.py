#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    i = len(my_list)
    if idx >= 0 and idx < i:
        del my_list[idx]
    return my_list
