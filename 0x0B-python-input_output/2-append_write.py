#!/usr/bin/python3
"""
Function that appends a string at the end of a file.
"""


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a file,
    and returns the number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        itappends = f.write(text)
    return itappends
