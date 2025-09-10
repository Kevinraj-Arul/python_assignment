import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/assignment9")))

from util import floor_array, ceil_array, rint_array

class TestRoundUtil(unittest.TestCase):
    def setUp(self):
        self.test_data = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]

    def test_floor(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(floor_array(self.test_data), expected)

    def test_ceil(self):
        expected = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(ceil_array(self.test_data), expected)

    def test_rint(self):
        expected = [1, 2, 3, 4, 6, 7, 8, 9, 10]
        self.assertEqual(rint_array(self.test_data), expected)

    def test_empty(self):
        self.assertEqual(floor_array([]), [])
        self.assertEqual(ceil_array([]), [])
        self.assertEqual(rint_array([]), [])

if __name__ == "__main__":
    unittest.main()