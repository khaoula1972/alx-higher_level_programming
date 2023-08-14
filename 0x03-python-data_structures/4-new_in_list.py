#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    L = my_list.copy()
    for x in my_list:
        if idx == my_list.index(x):
            L[idx] = element
            return (L)
        elif idx >= len(my_list):
            return (L)
        elif idx < 0:
            return (L)
