#!/usr/bin/python3
"""
Defines the append_after module.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends a line of text to a file.
    """
    with open(filename, 'r+', encoding='utf-8') as f:
        string = ""
        for line in f:
            string += line
            if search_string in line:
                string += new_string
        f.seek(0)
        f.write(string)
