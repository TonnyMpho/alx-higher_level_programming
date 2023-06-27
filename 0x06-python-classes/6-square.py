#!/usr/bin/python3
# 5-square.py - By TM
""" class Square that defines a square """


class Square:
    """ Instantiation with optional size and position"""
    def __init__(self, size=0, position=(0, 0)):
        """ Private instance attribute size and position"""
        self.__size = size
        self.__position = position

    """ getter to retrieve size """
    @property
    def size(self):
        return self.__size

    """ property setter to set size """
    @size.setter
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

    """ Getter to retrieve position """
    @property
    def position(self):
        return self.__position

    """ Property setter to set position """
    @position.setter
    def position(self, value):
        """
        position must be a tuple of 2 positive integers,
        otherwise raise a TypeError exception
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(n, int) and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """ Public instance method that returns the current square area """
    def area(self):
        square_area = self.__size * self.__size
        return square_area

    """
    Public instance method that prints
    in stdout the square with the character #
    """
    def my_print(self):
        """ if size is equal to 0, print an empty line """
        if self.__size == 0:
            print()
            return

        """  prints in stdout the square with the character # """
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end ="")
            print()
