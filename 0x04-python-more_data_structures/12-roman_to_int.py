#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string == None:
        return 0
    D = {'I': 1,'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s = 0
    for x in roman_string:
        s = s + D[x]
    return s
