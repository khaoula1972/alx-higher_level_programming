#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    l = 0;
    L = my_list.copy()
    while (L):
        l += 1
        L.pop()
    try:
        for i in range (x):
            print(my_list[i], end="")
        print()
        return (x)
    except IndexError:
        print()
        return (l)
