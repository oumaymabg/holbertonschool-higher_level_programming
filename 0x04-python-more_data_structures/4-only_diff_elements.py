#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    element = []
    for n in set_1:
        if n not in set_2:
            element.append(n)
    for n in set_2:
        if n not in set_1:
            element.append(n)
    return element
