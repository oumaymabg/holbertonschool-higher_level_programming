#!/usr/bin/python3
"""task-6:From_JSON_string_to_object"""
import json


def from_json_string(my_str):
    """from_json_string: function that returns an object
    represented by a JSON string
    """
    return json.loads(my_str)
