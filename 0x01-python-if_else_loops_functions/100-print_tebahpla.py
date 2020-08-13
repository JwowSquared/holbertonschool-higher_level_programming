#!/usr/bin/python3

for i in range(26):
    mod = 0
    if i % 2 == 1:
        mod = 32
    print("{}".format(chr(122 - i - mod)), end="")
