#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key in a_dictionary.keys():
        a_dictionary[key].pop()

    return a_dictionary
