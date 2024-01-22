#!/usr/bin/python3
import sys as s
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as e:
        print("Exception: {}".format(e), file=s.stderr)
    except TypeError as g:
        print("Exception: {}".format(g), file=s.stderr)
    return False
