#!/usr/bin/python3#!/usr/bin/python3
"""Class_Square_Num_4"""


class Square:
    """Private_instance_attribute"""

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # private attribute

    """Public instance method"""
    def area(self):
        return self.__size * self.__size

    """property"""
    def size(self):
        return self.__size

      """property setter"""
    def size(self, value):
        """instantiation with optional"""
        if type(size) != int:
            raise typeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        self.__size =value
