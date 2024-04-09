#!/usr/bin/python3
"""
Functionthat prints a square using the character #.
"""


def print_square(size):
    """
    Prints a square using the character #.
    Arguments:
        size(int): height and width of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        [print("#", end="") for y in range(size)]
        print("")
