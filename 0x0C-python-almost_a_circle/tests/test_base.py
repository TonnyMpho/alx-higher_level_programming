#!/usr/bin/python3
"""
Unittests for base
"""
import unittest
import os
import json
import csv
import turtle
from models.base import Base


class TestBase(unittest.TestCase):
    """
    unit test for Base class
    """

    def test_initialization(self):
        """
        test the initialization and see if the id
        class variable works
        """
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 12)


if __name__ == '__main__':
    unittest.main()
