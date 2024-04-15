#!/usr/bin/python3
"""
Defining module is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of,
    or if it's an instance of a class that inherited from.
    """
    return isinstance(obj, a_class)
