import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/assignment16")))
from util import can_pile

class TestPileUtil(unittest.TestCase):
    def test_sample_case_yes(self):
        cubes = [4, 3, 2, 1, 3, 4]
        self.assertEqual(can_pile(cubes), "Yes")

    def test_sample_case_no(self):
        cubes = [1, 3, 2]
        self.assertEqual(can_pile(cubes), "No")

    def test_single_cube(self):
        cubes = [5]
        self.assertEqual(can_pile(cubes), "Yes")

    def test_strictly_decreasing(self):
        cubes = [6, 5, 4, 3, 2, 1]
        self.assertEqual(can_pile(cubes), "Yes")

    def test_equal_cubes(self):
        cubes = [3, 3, 3, 3]
        self.assertEqual(can_pile(cubes), "Yes")

if __name__ == "__main__":
    unittest.main()