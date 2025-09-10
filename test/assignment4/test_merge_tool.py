import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/assigment4")))
from util import merge_the_tools

class TestMergeTheTools(unittest.TestCase):
    def test_sample_case(self):
        self.assertEqual(
            merge_the_tools("AABCAAADA", 3),
            ["AB", "CA", "AD"]
        )

    def test_all_unique(self):
        self.assertEqual(
            merge_the_tools("ABCDEFGH", 2),
            ["AB", "CD", "EF", "GH"]
        )

    def test_all_repeated(self):
        self.assertEqual(
            merge_the_tools("AAAA", 2),
            ["A", "A"]
        )

    def test_invalid_k(self):
        with self.assertRaises(ValueError):
            merge_the_tools("ABC", 4)

if __name__ == "__main__":
    unittest.main()