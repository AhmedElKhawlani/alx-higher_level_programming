#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    L = []
    for x in my_list:
        if x % 2 == 0:
            L.append(True)
        else:
            L.append(False)
    return L
