#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for n in range(0, x):
        try:
            print(my_list[n], end='')
        except valueError:
            break
    print()
