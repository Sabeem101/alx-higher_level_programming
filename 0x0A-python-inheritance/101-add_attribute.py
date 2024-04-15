#!/usr/bin/python3
"""
Adds an object.
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to object.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
