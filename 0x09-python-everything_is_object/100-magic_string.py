#!/usr/bin/python3
def magic_string():
    magic_string.nbr_print = getattr(magic_string, 'nbr_print', 0)
    return ', '.join(['BestSchool' for k in range(magic_string.nbr_print)])
