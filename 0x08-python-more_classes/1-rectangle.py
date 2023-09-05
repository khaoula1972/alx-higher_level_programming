#!/usr/bin/python3
"""
This contains a class called Rectangle
"""


class Rectangle:
    """
    Class: Rectangle

    Description: defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initialization ..

        Args:
            width: optional parameter describes width of rectangle
            height: optional parameter describes height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieve the width value
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Set the width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Retrieve the height value
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Set the height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
