#!/usr/bin/python3
"""
MyInt class.
"""


class MyInt(int):
    """
    MyInt class that inherits int.
    """
    def __eq__(self, x):
        """
        Defines module eq.
        """
        return not super().__eq__(x)

    def __ne__(self, x):
        """
        Defines module not eq.
        """
        return not super().__ne__(x)
