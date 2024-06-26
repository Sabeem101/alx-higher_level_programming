#!/usr/bin/python3
"""
Rectangle class inheriting base geometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class that inherits BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes rectangle from BaseGeometry.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Defines the area.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Rectangle with string.
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
