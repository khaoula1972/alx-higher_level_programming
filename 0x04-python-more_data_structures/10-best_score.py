#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return (None)
    big = 0
    bigger = ""
    for key in a_dictionary.keys():
        if big < a_dictionary[key]:
            big = a_dictionary[key]
            bigger = key
    return (bigger)
