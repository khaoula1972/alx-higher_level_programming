#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        v = fct(*args)
        return (v)
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return (None)
