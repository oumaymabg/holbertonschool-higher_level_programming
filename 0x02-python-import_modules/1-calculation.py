#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
a = 10
b = 5
somme = add(a, b)
som = sub(a, b)
somm = mul(a, b)
s = div(a, b)
print("{} + {} = {}".format(a, b, somme))
print("{} - {} = {}".format(a, b, som))
print("{} * {} = {}".format(a, b, somm))
print("{} / {} = {}".format(a, b, s))
