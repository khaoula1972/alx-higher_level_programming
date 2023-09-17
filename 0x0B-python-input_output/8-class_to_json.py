#!/usr/bin/python3
"""
This is a module conatining a function
"""


def class_to_json(obj):
    """
    a function that returns the dictionary description
    """

    if isinstance(obj, (int, str, bool)):
        return obj
    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    elif hasattr(obj, '__dict__'):
        {key: class_to_json(value) for key, value in obj.__dict__.items()}
        return {
                key: class_to_json(value)
                for key, value in obj.__dict__.items()
                }
    else:
        return str(obj)  # Handle other types as strings
