#!/usr/bin/python3
""" Module """


def read_file(filename=""):
    """
    function that reads a text file (UTF8) and prints it to stdout
    using the with statement
    """
    with open(filename, encoding="utf-8") as r_file:
        print(r_file.read)
