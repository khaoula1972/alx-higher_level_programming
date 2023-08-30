#!/usr/bin/python3
import math

"""
Class: MagicClass
"""


class MagicClass:
    """
    This class calculate the area and the perimeter of
    a circumference.
    """
    def __init__(self, radius=0):
        """
        Initialization of the circumference
        """
        self.radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.radius = radius

    def area(self):
        """
        This method calculate the area.
        """
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """
        This method calculates the perimeter
        """
        return ((2 * math.pi) * self.__radius)
