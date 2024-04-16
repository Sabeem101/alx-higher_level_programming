#!/usr/bin/python3
"""
Class student with public method to_json.
"""


class Student:
    """
    Class Student that has method to rint a dictionary
    representation of a Student instance.
    Attributes:
        first_name(str): student's first name.
        last_name(str): student's last name.
        age(int): student's age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new student class.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Gets a dictionary representation of the student class.
        """
        attri = self.__dict__.copy()

        if isinstance(attrs, list):
            for x in self.__dict__.keys():
                if x not in attrs:
                    del attri[x]
        return attri
