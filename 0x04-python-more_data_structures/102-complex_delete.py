#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    keys = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            keys.append(key)
    for x in keys:
        del a_dictionary[x]
    return a_dictionary
