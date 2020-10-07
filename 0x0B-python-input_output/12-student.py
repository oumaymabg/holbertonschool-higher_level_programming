#!/usr/bin/python3
"""task-12:student to JSON with filter 
based on 11-student.py"""


class Student:
    """class : student to json with filter"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and\
           all([isinstance(x, str) for x in attrs]):
            return {key: value for key, value in
                    self.__dict__.items() if key in attrs}
        return self.__dict__


