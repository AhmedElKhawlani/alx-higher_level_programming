#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for x in my_string:
        if x not in ('c', 'C'):
            new = new + x
    return new
