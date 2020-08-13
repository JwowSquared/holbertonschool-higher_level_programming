#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
descriptor = "Last digit of {:d} is {:d} and is "
mod = 10

if number < 0:
    mod = -10

if number % mod > 5:
    descriptor += "greater than 5"
elif number % mod == 0:
    descriptor += "0"
else:
    descriptor += "less than 6 and not 0"

print(descriptor.format(number, number % mod))
