import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/assignment5")))
from util import print_formatted

class TestFormatUtil(unittest.TestCase):

    def test_single_number(self):
        n = 1
        expected = ["1 1 1 1"]
        self.assertEqual(print_formatted(n), expected)

if __name__ == "__main__":
    unittest.main()