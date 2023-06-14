#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    a_dictionary = sorted(a_dictionary.keys())

    for key in a_dictionary:
        print("{}: {}".format(key, a_dictionary[key]))
