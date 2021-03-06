#!/usr/bin/python3


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    romans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    top = 1
    total = 0
    for c in reversed(roman_string):
        if c in romans:
            if romans[c] < top:
                total += romans[c] * -1
            else:
                top = romans[c]
                total += top
        else:
            return 0
    return total
