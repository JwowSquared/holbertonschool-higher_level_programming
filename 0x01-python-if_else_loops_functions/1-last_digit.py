#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
descriptor = "Last digit of {:d} is {:d} and is "

if number % 10 > 5:
    descriptor += "greater than 5"
elif number % 10 == 0:
    descriptor += "0"
else:
    descriptor += "less than 6 and not 0"

print(descriptor.format(number, number % 10))
