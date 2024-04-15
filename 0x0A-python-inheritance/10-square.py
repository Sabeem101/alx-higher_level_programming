#!/usr/bin/python3
"""
Square class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class inheriting Rectangle.
    """
    def __init__(self, size):
        """
        Initializing the square class.
        """
        self.__size = size
        self.integer_validator('size', self.__size)

    def area(self):
        """
        Defining area.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Usage of string.
        """
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
