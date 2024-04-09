#!/usr/bin/python3
"""
Adding __str__ methode in the rectangle class.
"""


class Rectangle:
    """
    Class the defines a rectangle.
    Attributes:
        width(int): rectangle width - private attribute.
        height(int): rectangle height  private attribute.
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
        """Property that sets the value of the rectangle width."""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Property that retirieves the rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter that sets the value of the rectangle height."""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """Instance methode that returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Instance methode that returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Standard methode that prints the rectangle with the character #"""

        rectangle = ""

        if self.__width == 0 or self.__height == 0:
            return rectangle

        x = 0
        while x <= self.__height:
            rectangle += "#" * self.__width
            if x < self.__height:
                rectangle += '\n'
            x += 1
        return rectangle
