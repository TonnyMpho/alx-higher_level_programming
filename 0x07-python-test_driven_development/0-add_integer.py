#!/usr/bin/python3

""" function that adds 2 integers. """

def add_integer(a, b=98):
    """
    Add two (2) integers.
    Args:
        a - (int or float): integer or float
        b - (int or float): integer or float - with a default value of 98
    Returns:
        total: int: The sun of a and b
    Raises:
        TypeError: if a or b is not an int or float
    """

    sum = 0

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    total = int(a) + int(b)
    return total
