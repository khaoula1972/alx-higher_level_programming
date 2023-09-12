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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        This calculates the area of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """
    This is rectangle's child
    """
    def __init__(self, size):
        """
        Initialization..
        """
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """
        This calculates the area of a square
        """
        return size * size

    def __str__(self):
        return "[Rectangle] {}/{}".format(size, size)
