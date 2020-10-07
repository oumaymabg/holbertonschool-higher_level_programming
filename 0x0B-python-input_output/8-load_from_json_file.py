#!/usr/bin/python3
"""task-8:Create_object_from_a_JSON_file"""
import json


def load_from_json_file(filename):
    """load_from_json_file: function that creates an
    object from a "JSON"file
    """
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
