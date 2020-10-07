#!/usr/bin/python3
"""task-10:class_to_JSON"""


def class_to_json(obj):
    """class_to_json:function that returns the dictionary
    description with simple data structure
    """
    return obj.__dict__
