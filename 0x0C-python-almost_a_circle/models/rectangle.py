#!/usr/bin/python3
"""
Rectangle class that inherits from Base.
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle that inherits from Base.
    Attributes:
        width(int): rectangle width.
        height(int): rectangle height.
        x(int): position of the rectangle in x.
        y(int): position of the rectangle in y.
        id(int): object id by Base.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Retrieves width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width value.
        """
        if isinstance(value, int) and not isinstance(value, bool):
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """
        Retrieves the height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height value.
        """
        if isinstance(value, int) and not isinstance(value, bool):
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """
        Retrieves x.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the value of x.
        """
        if isinstance(value, int) and not isinstance(value, bool):
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self, value):
        """
        Sets the value of y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the value of y.
        """
        if isinstance(value, int) and not isinstance(value, bool):
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """
        Public instance method that returns the rectangle area.
        """
        return self.__height * self.__width

    def __str__(self):
        """
        Method that returns the rectangle string representation.
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} " \
                f"- {self.__width}/{self.__height}"

    def display(self):
        """
        Method that prints the rectangle with character #.
        """
        Line = 0
        while Line < self.__y:
            print()
            Line += 1

        a = 1
        while a <= self.__height:
            b, c = 1, 1
            while c <= self.__x:
                print(" ", end='')
                c += 1
            while b <= self.__width:
                print("#", end='')
                b += 1
            print()
            a += 1

    def update(self, *args, **kwargs):
        """
        Method that update the values of rectangle.
        """
        arguments = 0
        for a in range(len(args)):
            arguments = 1
            if a == 0:
                self.id = args[a]
            elif a == 1:
                self.__width = args[a]
            elif a == 2:
                self.__height = args[a]
            elif a == 3:
                self.__x = args[a]
            elif a == 4:
                self.__y = args[a]
        if arguments == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value

    def to_dictionary(self):
        """
        Method that returns the rectangle dictionary representation.
        """
        return {"x": self.__x, "y": self.__y, "id": self.id,
                "height": self.__height, "width": self.__width}
