#!/usr/bin/python3
import random
number =random.randint(-10000, 10000)
l = int(repr(number)[-1]
if (l > 5):
print("Last digit of {:d} is {:d} and is greater than 5".format(number, l))
elif (l == 5):
print("Last digit of {:d} is {:d} and is 0".format(number, l))
elif ((l < 6) and (number != 0)):
print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, l))
