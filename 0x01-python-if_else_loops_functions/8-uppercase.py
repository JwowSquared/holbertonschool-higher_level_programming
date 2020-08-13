#!/usr/bin/python3


def uppercase(str):
    out = ""
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            out += chr(ord(str[i]) - 32)
        else:
            out += str[i]
    print("{}".format(out))
