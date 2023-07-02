#!/usr/bin/python3
""" function that prints a text with 2 new
lines after each of these characters: ., ? and :
"""

def text_indentation(text):
    """
    prints a text with 2 new lines after each
    of these characters: ., ? and :

    Args:
        text (str): text to add new lines

    Return:
        None - Print the string with the required space

    Raises:
        TypeError: the text must be a string
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    punctuation = [".", '?', ':']

    lines = []
    line = ""
    for char in text:
        line += char
        if char in punctuation:
            lines.append(line.strip())
            line = ""

    for line in lines:
        print(line)
        print()
