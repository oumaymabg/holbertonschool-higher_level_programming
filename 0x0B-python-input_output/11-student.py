#!/usr/bin/python3
"""task-11:Student to JSON """


class student:
    """Public instance attributes"""


def __init__(self, first_name, last_name, age):
    """Instantiation with first_name, last_name and age"""
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
"""Public method"""


def to_json(self):
    """that retrieves a dictionary representation of
    a Student instance
    """
    return self.__dict__
