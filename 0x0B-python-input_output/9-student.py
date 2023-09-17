#!/usr/bin/python3
"""
This module conatins a class
"""


class Student:
    """
    This is a class Student that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialization...
        """
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def to_json(self):
        """
        A public method that retrieves a dictionary representation of a Student
        """
        attributes_dict = {
                "first_name": self.__first_name,
                "last_name": self.__last_name,
                "age": self.__age
                }
        return attributes_dict
