#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        return(0)
    if len(tuple_a) > 2:
        return(tuple_a[:2])
