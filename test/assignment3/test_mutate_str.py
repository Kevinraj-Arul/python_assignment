import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/assignment3")))
from util import mutate_string

class TestMutateString(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(mutate_string("abracadabra", 5, "k"), "abrackdabra")

    def test_first_char(self):
        self.assertEqual(mutate_string("hello", 0, "H"), "Hello")

    def test_last_char(self):
        self.assertEqual(mutate_string("python", 5, "X"), "pythoX")

    def test_middle_char(self):
        self.assertEqual(mutate_string("world", 2, "R"), "woRld")

    def test_invalid_position(self):
        with self.assertRaises(ValueError):
            mutate_string("abc", 10, "z")

if __name__ == "__main__":
    unittest.main()