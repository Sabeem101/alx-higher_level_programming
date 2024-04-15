#!/usr/bin/python3
"""
is_same_class function.
"""


def is_same_class(obj, a_class):
    """
    Function that returns True if the object
    is exactly an instance of the specified
    class.
    """
    if type(obj) == a_class:
        return True
    return False
