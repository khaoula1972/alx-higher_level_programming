#!/usr/bin/python3
"""
This module contains a function
"""


def read_file(filename=""):
    """
    This is a function that reads a text file (UTF8) and prints it to stdout
    Args:
        filename: the file to be printed
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
