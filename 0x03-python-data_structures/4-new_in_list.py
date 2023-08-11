#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not (idx < 0 or idx >= len(my_list)):
        L = my_list.copy()
        L[idx] = element
    return (L)
