#!/usr/bin/python3
""" Module that contains a lookup function """


def lookup(obj):
    """
    function that returns the list of available
    attributes and methods of an object

    Args:
        obj: object
    Return:
        list of available attributes
    """
    return dir(obj)
