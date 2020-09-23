#!/usr/bin/python3
"""Class_Square_Num_3"""


class Square:
    """size:Private instance attribute"""

    def __init__(self, size=0):
        """Instantiation with optional size"""
        if type(size) != int:
            raise TypeError
        elif size < 0:
            raise ValueError
            self.__size = size
