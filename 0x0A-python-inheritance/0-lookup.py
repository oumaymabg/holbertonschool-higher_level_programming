#!/usr/bin/python3
"""lookup:a function that returns
the list of available attributes and
methods of an object"""


def lookup(obj):
    """obj:object /return a list object"""
    return dir(obj)
