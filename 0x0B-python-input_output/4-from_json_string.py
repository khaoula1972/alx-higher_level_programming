#!/usr/bin/python3
"""
This conains a function
"""
import json


def from_json_string(my_str):
    """
    a function that returns an object reresented by json
    """
    return json.loads(my_str)
