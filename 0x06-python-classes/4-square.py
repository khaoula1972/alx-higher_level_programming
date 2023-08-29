#!/usr/bin/python3
"""
A class: Square

A square is a four-sided polygon with all side of equal
length and all angles right angles.
"""


class Square:
    """
    This is Square class
    """

    def __init__(self, size=0):
        """
        Initialize a square with the given side length.

        Args:
            size: The length of all sides of the square.
            type: positive integer
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The length of all sides of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The length of all sides of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, (int)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Compute the area of a square with a given side length.

        Args:
            __size: the length of the side

        Returns:
                area of the square
        """
        return (self.__size ** 2)
