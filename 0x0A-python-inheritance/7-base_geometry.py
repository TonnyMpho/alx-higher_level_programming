#!/usr/bin/python3
""" Module with base class """


class BaseGeometry:
    """ class BaseGeometry """
    def area(self):
        """ public method that raises an Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Public instance methond that validates value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
