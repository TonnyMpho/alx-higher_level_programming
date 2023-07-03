#!/usr/bin/python3
""" class Rectangle that defines a rectangle """


class Rectangle:
    """
    class Rectangle:
    Defines or represents a rectangle
    """
    def __init__(self, width=0, height=0):
        """ instantiation with optional width and height """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ property width to retrieve the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ property setter - width to set the width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ property height to retrieve the width """
        return self.__height

    @height.setter
    def height(self, value):
        """
        property setter - height to set the height
        value passed must be an integer and >= 0
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
