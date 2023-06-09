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

    def area(self):
        """ Public instance method that returns the rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """ Public instance method that returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        print() and str() should print the rectangle with the character #
        if width and height equal to 0 return an empty string
        """
        rect = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            rect += "#" * self.__width
            if i != self.__height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """ return a string representation of the rectangle """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ called when an instance of Rectangle is deleted """
        print("Bye rectangle...")
