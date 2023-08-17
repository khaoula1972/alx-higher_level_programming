#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return (None)

    # Store the first value in the dic
    big = next(iter(a_dictionary))
    bigger = ""

    for key in a_dictionary.keys():
        if big < a_dictionary[key]:
            big = a_dictionary[key]
            bigger = key
    return (bigger)
