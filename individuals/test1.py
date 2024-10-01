# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from ind1 import RightTriangle


class RightTriangleTest(unittest.TestCase):
    def test_valid_initialization(self):
        triangle = RightTriangle(4, 6)
        self.assertEqual(triangle.first, 4)
        self.assertEqual(triangle.second, 6)

    def test_invalid_initialization(self):
        self.assertRaises(ValueError, RightTriangle, -1, 4)
        self.assertRaises(ValueError, RightTriangle, 4, -1)
        self.assertRaises(ValueError, RightTriangle, "bruh", 4)
        self.assertRaises(ValueError, RightTriangle, 4, "bruh")

    def test_hypotenuse(self):
        triangle = RightTriangle(3, 4)
        self.assertAlmostEqual(triangle(), 5.0)


if __name__ == "__main__":
    unittest.main()
