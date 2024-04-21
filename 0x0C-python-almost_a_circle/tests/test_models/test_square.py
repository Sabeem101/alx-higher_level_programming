#!/usr/bin/python3
"""
Square class unit tests.
"""
from models.base import Base
from models import square
import unittest
import json
Square = square.Square


class TestSquare(unittest.TestCase):
    """
    Functionality test.
    """
    @classmethod
    def setupclass(cls):
        """
        Sets up class tests.
        """
        Base._Base__nb_objects = 0
        cls.S1 = Square(3)
        cls.S2 = Square(4, 5)

    def idtest(self):
        """
        ID functionality test.
        """
        self.assertEqual(self.S1.id, 1)
        self.assertEqual(self.S2.id, 2)
    
    def sizetest(self):
        """
        Size functionality test.
        """
        self.assertEqual(self.S1.size, 1)
        self.assertEqual(self.S2.size, 2)

    def widthtest(self):
        """
        Width functionality test.
        """
        self.assertEqual(self.S1.width, 1)
        self.assertEqual(self.S2.width, 2)

    def heighttest(self):
        """
        Height functionality test.
        """
        self.assertEqual(self.S1.height, 1)
        self.assertEqual(self.S2.height, 2)

    def xtest(self):
        """
        X functionality test.
        """
        self.assertEqual(self.S1.x, 4)
        self.assertEqual(self.S2.x, 9)

    def ytest(self):
        """
        Y functionality test.
        """
        self.assertEqual(self.S1.y, 2)
        self.assertEqual(self.S2.y, 0)
