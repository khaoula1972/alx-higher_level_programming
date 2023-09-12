#!/usr/bin/python3
"""
This module contains a class to improve geometry
"""


class BaseGeometry:
    """
    This is a class o geometry
    """
    def area(self):
        """
        This method raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method validates value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    This is a class of rectangle
    """
    def __init__(self, width, height):
        """
        Initialization..
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
