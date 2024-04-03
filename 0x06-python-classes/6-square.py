#!/usr/bin/python3
"""
Adds an attribute in class Square.
"""


class Square:
    """
    Class that defines a square.
    Attributes:
    size(int): square size - private attribute.
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Property that retrieves the size"""
        return self.__size

    @property
    def position(self):
        """Property that retrieves the position"""
        return self.__position

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

    @position.setter
    def position(self, value):
        """Property setter that sets the position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value[0], int) and isinstance(value[1], int):
            if value[0] >= 0 and value[1] >= 0:
                self.__position = value
            else:
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Public instance method that prints the square with the character #"""
        if self.__size == 0:
            print()
            return
        L = 0
        while L < self.__position[1]:
            print()
            return
        x = 0
        while x <= self.__size:
            y, z = 1, 1
            while y <= self.__position[0]:
                print(" ", end='')
                y += 1
            while z <= self.__size:
                print("#", end='')
                z += 1
            print()
            x += 1
