#!/usr/bin/python3
"""
Class student with public method to_json.
"""


class Student:
    """
    Class Student that has method to print dictionary
    representation of a student instance.
    Attributes:
        first_name(str): student's first name.
        last_name(str): student's last name.
        age(int): student's age.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary representation of a student instance.
        """
        return self.__dict__
