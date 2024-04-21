#!/usr/bin/python3
"""
Square class that inherits from Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class square that inherits from Rectangle.
    Attributes:
        size(int): square size.
        x(int): position of the square in x.
        y(int): position of the square in y.
        id(int): object id by Base.
    """
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Retrieves the size.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the value of size.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Method that updates the values of square.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg in None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x == value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Method that returns the rectangle dictionary representation.
        """
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "size": self.width
        }

    def __str__(self):
        """
        String representation of square.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                self.width)
