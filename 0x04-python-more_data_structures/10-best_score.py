#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        key = None
        value = None
        for x in a_dictionary:
            if key == None:
                key = x
                value = a_dictionary[x]
            elif a_dictionary[x] > value:
                value = a_dictionary[x]
                key = x
        return key
    return None
