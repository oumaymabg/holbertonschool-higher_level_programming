#!/usr/bin/python3
"""class_My_list"""


class MyList(list):
    """Public instance method: that prints the list,
    but sorted (ascending sort)"""
    def print_sorted(self):
        """ that prints the list, but sorted (ascending sort)"""
        print(sorted(self))
