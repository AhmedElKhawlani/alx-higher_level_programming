#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    wa = 0
    d = 0
    for a, b in my_list:
        wa = wa + a * b
        d = d + b
    return wa / d
