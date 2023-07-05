#!/usr/bin/python3
"""unittests for max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Unittesting the function 6-max_integer
    """

    def test_empty_list(self):
        """ Testing for an empty list """
        self.assertIsNone(max_integer([]))

    def test_findmax_ordered(self):
        """ Testing list """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_findmax_unordered(self):
        """ Testing an unordered list """
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_findmax_beginning(self):
        """ Testing - max integer if its at the beginning of the list"""
        self.assertEqual(max_integer([4, 3, 1, 2]), 4)

    def test_findmax_negative(self):
        """ Test for max negative numbers """
        self.assertEqual(max_integer([-31, -4, -1, -10]), -1)

    def test_findmax_neg_1(self):
        """ Test for max only if theres one negative """
        self.assertEqual(max_integer([4, 3, -1, 2]), 4)

    def test_findmax_one(self):
        """ Test for max on a single list """
        self.assertEqual(max_integer([5]), 5)


if __name__ == '__main__':
    unittest.main()
