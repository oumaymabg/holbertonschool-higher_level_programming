#!/usr/bin/python3
"""task-2:Read n lines """


def read_lines(filename="", nb_lines=0):
    """read_lines:  a function that reads n lines of a text file (UTF8)
    and prints it to stdout
    """
    with open(filename, encoding="UTF-8") as file:
        if nb_lines <= 0:
            print(f.read(), end="")
            return
        for i in range(nb_lines):
            print(f.readline(), end="")
