#!/usr/bin/python3
# 103-magicClass by TM
"""
Python class MagicClass that does exactly the
same as the following Python bytecode:
"""

import math


class MagicClass:
    """ Private instance attribute: radius """
    def __init__(self, radius=0):
        self.__radius = 0

        """
        checking if radius is an integer or
        a float else raise an exception
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """ Return the area"""
        return self._radius ** 2 * math.pi

    def circumference(self):
        """ Returning the circumference """
        return 2 * math.pi * self.__radius
