#!/usr/bin/python3
"""
Adds print method in class Square.
"""


class Square:
    """
    Class that defines a square.
    Attributes:
        size(int): square size - private attribute.
    """

    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Public instance method that prints the square with character #"""
        if self.__size == 0:
            print()
        x = 1
        while x <= self.__size:
            y = 1
            while y <= self.__size:
                print("#", end='')
                y += 1
            print()
            x += 1

    @property
    def size(self):
        """Property that retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter that sets the value of the size"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")
