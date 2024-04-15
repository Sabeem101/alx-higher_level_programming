#!/usr/bin/python3
"""
Contains the mylist class.
"""


class MyList(list):
    """
    MyList class that inherits from list.
    """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        nlist = self.copy()
        nlist.sort()
        print(nlist)
