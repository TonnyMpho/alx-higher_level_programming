#!/usr/nin/python3
""" the “base” of all other classes in this project """


class Base:
    """
    the first class
    base class of all other clasess
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor - if id is not None, assign the
        public instance attribute id with this argument value
        otherwise, increment __nb_objects and assign the new
        value to the public instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
