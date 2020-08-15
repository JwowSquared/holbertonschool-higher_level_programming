#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    k = list(a_dictionary.keys())
    k.sort()
    for i in k:
        print("{}: {}".format(i, a_dictionary[i]))
