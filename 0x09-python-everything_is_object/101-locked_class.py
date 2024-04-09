#!/usr/bin/python3
"""
Defines a locked class.
"""


class LockedClass:
    """
    Prevents the user from dynamically creating new instances attributes,
    except if the new attribute is called first_name.
    """
    __unlock__ = ["first_name"]
