import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/assignment10")))
from util import min_max_operation

class TestMinMaxOperation(unittest.TestCase):
    def test_sample_case(self):
        arr = [
            [2, 5],
            [3, 7],
            [1, 3],
            [4, 0]
        ]
        self.assertEqual(min_max_operation(arr), 3)

    def test_single_row(self):
        arr = [[10, 20, 30]]
        self.assertEqual(min_max_operation(arr), 10)

    def test_all_same(self):
        arr = [[2, 2], [2, 2], [2, 2]]
        self.assertEqual(min_max_operation(arr), 2)

if __name__ == "__main__":
    unittest.main()