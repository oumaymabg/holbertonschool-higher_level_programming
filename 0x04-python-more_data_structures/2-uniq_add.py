#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    new_add = set(my_list)
    for number in new_add:
        add += number
    return add
