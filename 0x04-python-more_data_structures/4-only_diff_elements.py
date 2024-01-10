#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_3 = set()
    for x in set_1:
        if x not in set_2:
            set_3.add(x)
    for x in set_2:
        if x not in set_1:
            set_3.add(x)
    return set_3
