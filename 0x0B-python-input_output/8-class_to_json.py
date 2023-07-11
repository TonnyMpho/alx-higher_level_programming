#!/usr/bin/python3
""" JSON serialization of an object """


def class_to_json(obj):
    """
    function that returns the dictionary description
    with simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object
    """
    if isinstance(obj, (list, dict, str, int, bool)):
        return obj

    if isinstance(obj, object):
        attr = {}
        for i, val in obj.__dict__.items():
            attr[i] = class_to_jason(value)
        return attr
    return None
