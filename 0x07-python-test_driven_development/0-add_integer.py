#!/usr/bin/python3
"""

Module that contains a function to sum two integers

"""


def add_integer(a, b=98):
    """Function that returns the sum of two integers.
    Args:
        a: First integer;
        b: Second integer.
    Returns:
        The sum of a and b.
    Raises:
        TypeError if a or b are not real numbers
    """
    if (not isinstance(a, int)) and (not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int)) and (not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
