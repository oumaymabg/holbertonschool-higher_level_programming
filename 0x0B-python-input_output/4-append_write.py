#!/usr/bin/python3
"""task-4:append_file"""


def append_write(filename="", text=""):
    """append_file:a function that appends a string at the en of a text file
    (UTF8) and returns the number pf characters added"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
