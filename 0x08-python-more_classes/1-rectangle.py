#!/usr/bin/python3
"""class_Real_definition_of_a_rectangle"""


class Rectangle:
    """Private instance attribute:width"""
    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width  # private attribute

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    """Private instance attribute:height"""

    @property
    def height(self):
        return self.__height  # private attribute

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
