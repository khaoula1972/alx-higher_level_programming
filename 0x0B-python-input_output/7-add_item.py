#!/usr/bin/python3
"""
This module contains a script that loads, adds, and saves files
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    try:
        existing_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_list = []

    args = sys.argv[1:]
    existing_list.extend(args)

    save_to_json_file(existing_list, "add_item.json")
