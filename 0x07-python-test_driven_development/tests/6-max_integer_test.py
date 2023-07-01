#!/usr/bin/python3
"""unittests for max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def empylist(self):
        self.assertEqual(max_integer([]), None)

    def findmax_ordered(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def findmax_unordered(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def findmax_begging(self):
        self.assertEqual(max_integer([4, 3, 1, 2]), 4)

if __name__=='__main__':
    unittest.main()
