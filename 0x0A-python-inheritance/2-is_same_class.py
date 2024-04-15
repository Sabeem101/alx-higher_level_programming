#!/usr/bin/python3
"""
Module definition is_same_class.
"""


def is_same_class(obj, a_class):
    """
    Function that returns True if the object
    is exactly an instance of the specified
    class.
    """
    return (type(obj) == a_class)
