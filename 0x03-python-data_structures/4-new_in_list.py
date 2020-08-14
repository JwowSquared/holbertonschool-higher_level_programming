#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    new = []
    for i in range(len(my_list)):
        if i == idx:
            new.append(element)
        else:
            new.append(my_list[i])
    return new
