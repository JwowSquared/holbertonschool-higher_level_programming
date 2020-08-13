#!/usr/bin/python3
import random
number = random.randint(-10, 10)
descriptor = "is "

if number > 0:
	descriptor += "positive"
elif number < 0:
	descriptor += "negative"
else:
	descriptor += "zero"

print("{:d} {}".format(number, descriptor))
