#!/usr/bin/pyhton3
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
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Defining area.
        """
        return self.__size ** 2

    def __str__(self):
        """
        String usage.
        """
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
