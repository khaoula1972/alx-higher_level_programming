#!/usr/bin/python3
"""
This module contains a file function
"""


def append_write(filename="", text=""):
    """
    This is a function that append a string to a text file (UTF8)
    Args:
        filename: the file
        text: text to append
    """
    with open(filename, 'a', encoding='utf-8') as file:
        num = file.write(text)
    return num
