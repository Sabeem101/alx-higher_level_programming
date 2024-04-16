#!/usr/bin/python3
"""
Function that writes to a text file.
"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file,
    and returns the number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        itwrites = f.write(text)
    return itwrites
