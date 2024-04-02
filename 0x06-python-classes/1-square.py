#!/usr/bin/python3
"""
Defining an attribute to class Square.
"""


class Square:
    """
    Class that defines a square.
    Attributes:
        size(int): size of the first square - private attribute.
    """

    def __init__(self, size):
        self.__size = size
