#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        d = 0
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            d += 1
        if d != 0:
            print()
    except (TypeError, ValueError):
        pass

    return (d)
