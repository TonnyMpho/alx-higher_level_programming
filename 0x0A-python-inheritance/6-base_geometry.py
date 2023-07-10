#!/usr/bin/python3
""" Module with base class """


class BaseGeometry:
    """ class BaseGeometry """
    def area(self):
        """ public method that raises an Exception """
        raise Exception("area() is not implemented")
