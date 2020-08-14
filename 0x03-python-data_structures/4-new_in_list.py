#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    new = my_list.copy()
    for i in range(len(new)):
        if i == idx:
            new[i] = element
            break
    return new
