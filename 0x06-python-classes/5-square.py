#!/usr/bin/python3
"""Class_Square_Num_4"""


class Square:
    """Private_instance_attribute"""

    def __init__(self, size=0):
        self.__size = size  # private attribute

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        """Public instance method:that prints in stdout the square"""
        if self.__size > 0:
            for row in range(self.__size):
                for column in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """set_size instantiation with optional"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")
        self.__size = value
