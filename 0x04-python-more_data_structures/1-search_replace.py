#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if search in my_list:
        L = [replace if i == search else i for i in my_list.copy()]
        return(L)
