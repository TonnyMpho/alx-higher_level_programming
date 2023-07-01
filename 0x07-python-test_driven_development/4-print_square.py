#!/usr/bin/python3
""" function that prints a square with the character # """

def print_square(size):
    """
    Prints a squre with the character #

    Args:
        size (int): size of the square

    Return:
        None - prints the square

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """

    if type(size) != int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
        print()
    print()
