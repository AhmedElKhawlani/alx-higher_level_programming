#!/usr/bin/python3
def search_replace(my_list, search, replace):
    L = my_list.copy()
    for i in range(len(L)):
        if L[i] == search:
            L[i] = replace
    return L
