#!/usr/bin/python3

"""
Class: MagicClass
"""

import math


class MagicClass:
    """
    This class calculate the area and the perimeter of
    a circumference.
    """

    def __init__(self, radius=0):
        """
        Initialization of the circumference.

        Args:
        radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        This method calculate the area.
        """
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """
        This method calculates the perimeter
        """
        return (2 * math.pi * self.__radius)
