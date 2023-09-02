#!/usr/bin/python3


"""
This module contains a function that treats identation
"""


def text_indentation(text):
    """
    Function: text_indentation

    Description: a function that prints a text with 2 new \
            lines after each of these characters: ., ? and :
    Args:
        text: the text to be indented

    Raises:
        TypeError :  in case we passed a non string argument

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # To strip the text from any spaces in the begining or end :
    text = text.strip()

    # The flag is to check if the special characters was printed
    flag = 0

    # A counter
    i = 0

    while i < len(text):
        if text[i] == ":" or text[i] == "?" or text[i] == ".":
            print(text[i])
            print()
            i += 1
            flag = 1
        else:
            if flag == 1 and text[i] == " ":
                i += 1
                continue

            else:
                print(text[i], end="")
                i += 1
                flag = 0
