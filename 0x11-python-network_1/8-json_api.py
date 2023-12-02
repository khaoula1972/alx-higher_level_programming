#!/usr/bin/python3
"""
    Script that takes in a letter and sends a POST request to
    https://0.0.0.0:5000/search_user with the letter as a parameter
"""


import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        p = {'q': sys.argv[1]}
    else:
        p = {'q': ""}
    r = requests.post("http://0.0.0.0:5000/search_user", data=p)
    try:
        r_js = r.json()
        if r_js == {}:
            print("No result")
        else:
            print("[{}] {}".format(r_js['id'], r_js['name']))
    except ValueError:
        print("Not a valid JSON")
