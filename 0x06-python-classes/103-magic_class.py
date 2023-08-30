#!/usr/bin/python3
import math


class MagicClass:
    """
    This class calculate the area and the perimeter of
    a circumference."""
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    """ This method calculate the area. """
    def area(self):
        return ((self.__radius ** 2) * math.pi)

    """ This method calculates the perimeter """
    def circumference(self):
        return (2 * math.pi * self.__radius)
