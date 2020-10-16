#!/usr/bin/python3
"""class_base_1"""


from json import dumps, loads
import csv


class Base:
    """private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id not None:
            self.id = id
        else:
            base.__nb_objects += 1
            self.id = Base.__nb_objects
