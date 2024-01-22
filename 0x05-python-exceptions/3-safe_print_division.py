#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        d = a / b
    except ZeroDivisionError:
        pass
    finally:
        if b == 0:
            d = None
        print("Inside result: {}."format(d))
        return d
