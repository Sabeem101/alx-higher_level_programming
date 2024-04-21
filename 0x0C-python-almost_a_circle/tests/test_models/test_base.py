#!/usr/bin/python3
"""
Unit testing for Base.
"""
from models import base
import unittest
import json
Base = base.Base


class TestBase(unittest.TestCase):
    """
    Base class tests.
    """
    def too_many_args(self):
        """
        Arguments test.
        """
        with self.assertRaises(TypeError):
            B = Base(1, 1)

    def no_id(self):
        """
        ID availability test.
        """
        B = Base()
        self.assertEqual(B.id, 1)

    def sets_id(self):
        """
        Available ID test.
        """
        B98 = Base(98)
        self.assertEqual(B98.id, 98)

    def priv_nb(self):
        """
        Private nb_objects test.
        """
        B = Base(3)
        with self.assertRaises(AttributeError):
            print(B.nb_objects)
        with self.assertRaises(AttributeError):
            print(B.__nb_objects)

    def JSON_string(self):
        """
        Regular to json string test.
        """
        Base._Base__nb_objects = 0
        dt1 = {"id": 7, "width": 3, "height": 4, "x": 5, "y": 6}
        dt2 = {"id": 4, "width": 4, "height": 5, "x": 6, "y": 0}
        jstr = Base.to_json_string([dt1, dt2])
        self.assertTrue(type(jstr) is str)
        D = json.loads(jstr)
        self.assertEqual(D, [dt1, dt2])
