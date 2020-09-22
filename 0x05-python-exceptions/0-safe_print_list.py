#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    prints = 0
    for n in range(0, x):
        try:
            print(my_list[n], end='')
            prints += 1
        except valueError:
            break
    print()
    return(prints)
