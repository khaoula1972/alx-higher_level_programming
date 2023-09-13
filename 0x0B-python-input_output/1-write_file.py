#!/usr/bin/python3
"""
This module contains a file function
"""


def write_file(filename="", text=""):
    """
    This is a function that writes a string to a text file (UTF8)
    Args:
        filename: the file
        text: text to overwrite
    """
    with open(filename, 'w', encoding='utf-8') as file:
        num = file.write(text)
    return num
