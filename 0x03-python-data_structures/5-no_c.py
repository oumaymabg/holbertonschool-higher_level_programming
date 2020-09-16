#!/usr/bin/env python3
def no_c(my_string):
    N_char = ""
    for new_char in my_string:
        if new_char != 'c' and new_char != 'C':
            N_char += new_char
    return(N_char)
