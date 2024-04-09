#!/usr/bin/python3
"""
Unittests for max_integer([...]).
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Defines unittests for max_integer([..])."""
    def tlist(self):
        """Tests a list of integers."""
        order = [1, 2, 3, 4]
        self.assertEqual(max_integer(order), 4)

    def tunlist(self):
        """Tests an unordered list of integers."""
        unorder = [1, 3, 4, 2]
        self.assertEqual(max_integer(unorder), 4)

    def tmax_first(self):
        """Tests a list with a max value at the beginning."""
        max_first = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_first), 4)

    def tempty_list(self):
        """Tests an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def tone_elem(self):
        """Tests a list with a single elemnt."""
        one_el =[4]
        self.assertEqual(max_integer(one_el), 7)

    def tfloats(self):
        """Tests a list of floats."""
        flts = [1.43, 5.22, -9.765, 25.3, 9.0]
        self.assertEqual(max_integer(flts), 25.3)

    def tints_floats(self):
        """Tests a list of ints and floats."""
        ints_floats = [5, 4.2, -3, 22, 0]
        self.assertEqual(max_integer(ints_floats), 4.2)

    def tstring(self):
        """Tests a string."""
        strn = "Sabeem"
        self.assertEqual(max_integer(strn), 'r')

    def tlist_string(self):
        """Tests a list of strings."""
        strns = ["Sabeem", "is", "my", "name"]
        self.assertEqual(max_integer(strns), "name")

    def tempty_string(self):
        """Tests an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
