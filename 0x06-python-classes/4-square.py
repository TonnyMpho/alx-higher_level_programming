#!/usr/bin/python3
# 3-square.py - By TM
""" class Square that defines a square """


class Square:
    """ Instantiation with optional size """
    def __init__(self, size=0):
        """ Private instance attribute size"""
        self.__size = size

    """ getter to retrieve size """
    def size(self):
        return self.__size

    """ property setter to set size """
    def size(self, value):
        """
        Checking if size is an integer or not less than 0
        otherwise raise an Exception
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """ Public instance method that returns the current square area """
    def area(self):
        square_area = self.__size * self.__size
        return square_area
