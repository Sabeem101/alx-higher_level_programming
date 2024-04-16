#!/usr/bin/python3
"""
Function that returns JSON representation.
"""
import json


def to_json_string(my_obj):
    """
    Function that returns a JSON representation
    of an object.
    """
    return json.dumps(my_obj)
