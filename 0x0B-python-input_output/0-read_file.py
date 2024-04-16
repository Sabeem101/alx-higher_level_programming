#!/usr/bin/python3
"""
Function that reads a text file.
"""


def read_file(filename=""):
    """
    Function that reads a file,
    and prints its content to stdout.
    """
    with open(filename, encoding='utf-8') as f:
        reads_data = f.read()
        print(reads_data, end='')
