#!/usr/bin/python3
"""
Adding a class methode to the rectangle class.
"""


class Rectangle:
    """
    Class that defines the rectangle.
    Attributes:
        width(int): rectangle width - private attribute.
        height(int): rectangle height - private attribute.
        number_of_instances(int): number of instances - public attribute.
        print_symbol(any): symbol used to print the rectangle - public attribute.
    """
    number_of_instances = 0
    print_symbol = "#"

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
            else:
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

        x = 1
        while x <= self.__height:
            rectangle += str(self.print_symbol) * self.__width
            if x < self.__height:
                rectangle += '\n'
            x += 1
        return rectangle

    def __repr__(self):
        """Standard methode that prints the representation of the rectangle."""
        return "Rectangle(" + str(self.__width) + \
                ", " + str(self.__height) + ")"

    def __del__(self):
        """Destructor methode that prints a string when the object is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
       """Static methode that returns the biggest rectangle based on area."""
       if not isinstance(rect_1, Rectangle):
           raise TypeError("rect_1 must be an instance of Rectangle")
       if not isinstance(rect_2, Rectangle):
           raise TypeError("rect_2 must be an instance of Rectangle")

       if rect_1.area() > rect_2.area():
           return rect_1
       elif rect_1.area() < rect_2.area():
           return rect_2
       elif rect_1.area() == rect_2.area():
           return rect_1

    @classmethod
    def square(cls, size=0):
        """
        Class methode that prints a new rectangle instance
                with width == height == size
        """
        return (cls(size,size))
