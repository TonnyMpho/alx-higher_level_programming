#!/usr/bin/python3
"""unittests for max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Unittesting the function 6-max_integer
    """

    def empylist(self):
        """ Testing for an empty list """
        self.assertNone(max_integer([]), None)

    def findmax_ordered(self):
        """ Testing list """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def findmax_unordered(self):
        """ Testing an unordered list """
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def findmax_beginning(self):
        """ Testing - max integer if its at the beginning of the list"""
        self.assertEqual(max_integer([4, 3, 1, 2]), 4)

if __name__=='__main__':
    unittest.main()
