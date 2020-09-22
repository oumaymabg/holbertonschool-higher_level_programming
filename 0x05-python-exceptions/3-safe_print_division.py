#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        RT = a/b
    except ZeroDivisionError:
        RT = none
    finally:
        print("Inside result: {}".format(RT))
        return(RT)
