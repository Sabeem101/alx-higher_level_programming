#!/usr/bin/python3
"""
Retangle inheriting base geometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits BaseGeometry.
    Attributes:
        width(int): rectangle width - private attribute.
        height(int): rectangle height - private attribute.
    """
    def __init__(self, width, height):
            self.integer_validator("width", width)
            self.integer_validator("height", height)
            self.__width = width
            self.__height = height
