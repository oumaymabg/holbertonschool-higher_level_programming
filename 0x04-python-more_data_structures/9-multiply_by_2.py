#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mult = {}
    for n, x in a_dictionary.items():
        mult[n] = a_dictionary[n] * 2
    return mult
