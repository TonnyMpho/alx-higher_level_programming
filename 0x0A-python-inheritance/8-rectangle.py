#!/usr/bin/python3
"""
Module with class that inherits from
BaseGeometry (7-base_geometry.py).
"""
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle that inherits from BaseGeometry """
    def __init__(self, width, height):
        """
        Instantiation with width and height
        width and height validated by integer_validator
        inherited from BaseGeometry
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
