#!/usr/bin/python3
"""task-13:Student to disk and reload
based on 12-student.py"""


class Student:
    """class : student to json with filter"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        dictionary = {}
        for i in attrs:
            if i in self.__dict__.keys():
                dictionary[i] = self.__dict__[i]
        return dictionary

    def reload_from_json(self, json):
        for k, value in json.items():
            self.__dict__[k] = value
