#!/usr/bin/python3
"""
Function that creates an object.
"""
import json


def load_from_json_file(filename):
    """
    Function that creates an Object using a JSON file.
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        itreads = f.read()
    return json.loads(itreads)
