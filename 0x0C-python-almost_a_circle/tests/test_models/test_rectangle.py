#!/usr/bin/python3
"""
Rectangle class tests.
"""
from models import rectangle
from models.base import Base
import unittest
import json
Rectangle = rectangle.Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test cases for Rectangle class.
    """
    def classsetup(cls):
        """
        Sets up the class.
        """
        Base._Base__nb_objects = 0
        cls.R1 = Rectangle(5, 5)
        cls.R2 = Rectangle(5, 4, 3)

    def IDtest(self):
        """
        ID functionality test.
        """
        self.assertEqual(self.R1.id, 1)
        self.assertEqual(self.R2.id, 2)

    def widthtest(self):
        """
        Width functionality test.
        """
        self.assertEqual(self.R1.width, 10)
        self.assertEqual(self.R2.width, 4)

    def heighttest(self):
        """
        Height functionality test.
        """
        self.assertEqual(self.R1.height, 10)
        self.assertEqual(self.R2.height, 6)

    def xtest(self):
        """
        X functionality test.
        """
        self.assertEqual(self.R1.x, 0)
        self.assertEqual(self.R2.x, 7)

    def ytest(self):
        """
        Y functionality test.
        """
        self.assertEqual(self.R1.y, 0)
        self.assertEqual(self.R2.y, 0)
