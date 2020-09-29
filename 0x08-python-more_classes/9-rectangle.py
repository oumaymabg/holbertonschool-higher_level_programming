#!/usr/bin/python3
"""class_Real_definition_of_a_rectangle"""


class Rectangle:
    """Private instance attribute:width"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width  # private attribute

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
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
    """Public instance method"""

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = self.__height * 2 + self.__width * 2
        return perimeter

    def __str__(self):
        """ prints in stdout the Rectangle with the character # """
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle

        for height in range(self.__height):
            for width in range(self.__width):
                rectangle += str(self.print_symbol)
            rectangle += '\n'
        rectangle = rectangle[:-1]
        return rectangle

    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ an instance of Rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        return print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """Static method: returns the biggest rectangle based on the area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
