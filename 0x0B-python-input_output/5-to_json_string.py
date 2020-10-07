#!/usr/bin/python3
"""task-5:To JSON string"""
import json


def to_json_string(my_obj):
    """JSON:s a syntax for storing and exchanging data
    my_obj: object
    Write a function that returns the JSON representation
    of an object (string)
    """
    return json.dumps(my_obj)
