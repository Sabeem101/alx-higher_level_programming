#!/usr/bin/python3
"""
Defining two attributes for the rectangle class.
"""


class Rectangle:
    """
    Class that defines a rectangle.
    Attributes:
        width(int): the rectangle width - private attribute.
        height(int): the rectangle height - private attribute.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property that retrieves the rectangle width."""
        return self.__width
    @width.setter
    def width(self, value):
        """Property setter that sets the value of the rectangle width."""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Property that retrieves the rectangle height."""
        return self.__height
    @height.setter
    def height(self, value):
        """Property setter that sets the value of the rectangle height."""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
        else:
            raise TypeError("height must be an integer")
