#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or not my_list:
        return (0)
    av = 0
    s = 0
    for score, weight in my_list:
        av += score * weight
        s += weight

    if s == 0:
        return (0)

    return (av / s)
