#!/usr/bin/python3
""" Module 13. Search and update """


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of text to a file, after
    each line containing a specific string
    """
    string = ""
    with open(filename, encoding='utf-8') as r_file:
        for line in r_file:
            string += line
            if search_string in line:
                string += new_string

    with open(filename, 'w', encoding='utf-8') as w_file:
        w_file.write(string)
