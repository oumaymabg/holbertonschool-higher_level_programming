#!/usr/bin/python3
"""class_BaseGeometry_num3"""


class BaseGeometry:
    """Public instance method"""

    def area(self):
        """that raises an Exception with the message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ that raise a TypeError;ValueError exception, with the message"""
        if type(value) is not int:
            raise TypeError("<name> must be an integer".format(name))
        if value <= 0:
            raise ValueError("<name> must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry class"""
    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
