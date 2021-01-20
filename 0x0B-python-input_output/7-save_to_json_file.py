#!/usr/bin/python3
"""task-7:Save_object_to_a_file"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file: function that writes an object to a text file
    using a JSON representation
    """
    with open(filename, mode="w", encoding='utf-8') as my_file:
        json.dump(my_obj, my_file)
