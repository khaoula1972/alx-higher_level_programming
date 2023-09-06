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

    copy_text = text[:]

    for d in (".", "?", ":"):
        list_text = copy_text.split(d)
        copy_text = ""
        for i in list_text:
            i = i.strip(" ")
            copy_text = i + d if copy_text is "" else copy_text + "\n\n" + i + d
    
    print(copy_text[:-3], end="")
