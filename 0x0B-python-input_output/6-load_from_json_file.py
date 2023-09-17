#!/usr/bin/python3
"""
This module contains a function that creates an object
"""
import json


def load_from_json_file(filename):
    """
    This is a function that creates an Object fro-m a “JSON file”
    """
    with open(filename, 'r', encoding='utf-8') as file_t:
        return json.load(file_t)
