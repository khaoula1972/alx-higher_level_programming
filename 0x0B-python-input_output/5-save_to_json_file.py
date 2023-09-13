#!/usr/bin/python3
"""
This conains a function
"""
import json


def save_to_json_file(my_obj, filename):
    """
    a function that writes an object reresented by json
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
