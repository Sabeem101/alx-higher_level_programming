#!/usr/bin/python3
"""
Adds arguments to a Python list.
"""
import sys

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file


open("add_item.json", "a")
try:
    args = load_from_json_file("add_item.json")
except ValueError:
    args = []
save_to_json_file(args + sys.argv[1:], "add_item.json")
