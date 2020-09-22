#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        RT = a/b
    except ZeroDivisionError:
        RT = None
    finally:
        print("Inside RT: {}".format(RT))
        return(RT)
