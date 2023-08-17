#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy = dict()
    for key in a_dictionary:
        copy[key] = a_dictionary[key]* 2
    return (copy)
