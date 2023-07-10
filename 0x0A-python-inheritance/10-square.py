#!/usr/bin/python3
"""
module with a class that inherits from
Rectangle (9-rectangle.py)
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Square that inherits from Rectangle """
    def __init__(self, size):
        """
        Instantiation with size
        validated by integer_validator
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ Returns the area of a Square """
        return self.__size * self.__size
