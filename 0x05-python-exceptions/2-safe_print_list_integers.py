#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    cpt = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end='')
            cpt = cpt + 1
        except TypeError:
            pass
        except ValueError:
            pass
        i = i + 1
    if cpt > 0:
        print()
    return cpt
