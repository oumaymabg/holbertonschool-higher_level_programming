#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10 if number > 0 else -number % 10
if (l >= 5):
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, l))
if (l == 0):
    print("Last digit of {:d} is {:d} and is 0".format(number, l))
if ((l < 6) and (l != 0)):
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, l))
