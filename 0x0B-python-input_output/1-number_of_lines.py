#!/usr/bin/python3
"""task-1:Number_of_lines"""


def number_of_lines(filename=""):
    """number_of_file:a function that returns the number 
    of lines of a text file
    """
    counter = 0
    with open(filename, encoding="UTF-8") as file:
        for n in file:
            if n:
                counter += 1
    return counter
