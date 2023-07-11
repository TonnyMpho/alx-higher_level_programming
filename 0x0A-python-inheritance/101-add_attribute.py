#!/usr/bin/python3
""" Module for `add_attribute` """


def add_attribute(obj, attr, value):
    """
    function that adds a new attribute to an object if it’s possible.
    Raise a TypeError exception if the object can’t have new attribute
    """
    if hasattr(obj, attr):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value)
