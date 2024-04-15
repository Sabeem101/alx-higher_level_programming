#!/usr/bin/python3
"""
Defining integer validator of class base geometry.
"""


class BaseGeometry:
    """
    Class base geometry with public instance method area and integer validator.
    """
    def area(self):
        """
        Public instance
        Raise:
            Exception: Area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
