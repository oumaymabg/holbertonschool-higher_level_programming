#!/usr/bin/python3
"""task-3:write_file"""


def write_file(filename="", text=""):
    """write_file:a function that writes a string to a text file (UTF8) and
    returns the number of characters written
    """
    with open(filename, "w", encoding="UTF-8") as file:
        return file.write(text)
