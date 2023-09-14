#!/usr/bin/python3
import json
"""
This module contains a function that creates an object
"""


def load_from_json_file(filename):
    """
    This is a function that creates an Object from a “JSON file”
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
