#!/usr/bin/python3
"""
This contains a class called Rectangle
"""


class Rectangle:
    """
    Class: Rectangle

    Description: defines a rectangle
    """
    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initialization ..

        Args:
            width: optional parameter describes width of rectangle
            height: optional parameter describes height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        Method that returns  the rectangle area
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Method that returns the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Method that returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() < rect_2.area():
            return (rect_2)
        return (rect_1)

    @classmethod
    def square(cls, size=0):
        """
        Method that returns a new Rectangle instance with :
                        width == height == size
        """
        return (cls(size, size))

    def __str__(self):
        """
        Method that allow printable rectangle with #
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        string = ""
        for _ in range(self.__height):
            string += str(self.print_symbol) * self.__width + "\n"
        return (string[:-1])

    def __repr__(self):
        """
        Method that returns the string presentation of the instance
        """
        return ("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        """
        Method that print a message when an instance of Rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
