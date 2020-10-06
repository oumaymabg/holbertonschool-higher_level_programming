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
