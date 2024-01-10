#!/usr/bin/python3
def uniq_add(my_list=[]):
    used = []
    s = 0
    for x in my_list:
        if x not in used:
            s = s + x
            used.append(x)
    return s
