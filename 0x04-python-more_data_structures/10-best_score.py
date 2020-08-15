#!/usr/bin/python3


def best_score(a_dictionary):
    out = None
    best = 0
    if a_dictionary is not None:
        for i in a_dictionary:
            if a_dictionary[i] > best:
                best = a_dictionary[i]
                out = i
    return out
