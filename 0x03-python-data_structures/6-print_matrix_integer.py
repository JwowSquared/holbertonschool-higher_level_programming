#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        if list == []:
            print("")
            continue
        for i in range(len(list) - 1):
            print("{:d} ".format(list[i]), end="")
        print("{:d}".format(list[-1]))
