#!/usr/bin/python3
# 3-square.py - By TM
""" class Square that defines a square """


class Square:
    """ Instantiation with optional size """
    def __init__(self, size=0):
        """ Private instance attribute size"""
        """
        Checking if size is an integer or not less than 0
        otherwise raise an Exception
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """ Public instance method that returns the current square area """
    def area(self):
        square_area = self.__size * self.__size
        return square_area
