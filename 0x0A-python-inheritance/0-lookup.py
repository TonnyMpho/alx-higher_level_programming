#!/usr/bin/python3

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
