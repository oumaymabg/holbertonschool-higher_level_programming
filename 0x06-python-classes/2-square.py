#!/usr/bin/python3
"""Class_Square_Num_3"""


class Square:
    """size:Private instance attribute"""

    def __init__(self, size=0):
        """Instantiation with optional size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # private attribute
