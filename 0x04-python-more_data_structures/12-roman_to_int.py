#!/usr/bin/python3
def roman_to_int(roman_string):
    if not (isinstance(roman_string, str)) or roman_string is None:
        return 0
    D = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s = 0
    last = 0
    i = len(roman_string) - 1
    for j in range(i, -1, -1):
        x = D[roman_string[j]]
        if x >= last:
            s = s + x
        else:
            s = s - x
        last = x
    return s
