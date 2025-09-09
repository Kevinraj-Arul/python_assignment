import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/assignment2")))
from util import find_runner_up

class TestRunnerUp(unittest.TestCase):
    def test_sample_case(self):
        self.assertEqual(find_runner_up([2, 3, 6, 6, 5]), 5)

    def test_all_unique(self):
        self.assertEqual(find_runner_up([10, 20, 30, 40]), 30)

    def test_with_negatives(self):
        self.assertEqual(find_runner_up([-5, -1, -3, -1]), -3)

    def test_all_same(self):
        self.assertIsNone(find_runner_up([5, 5, 5, 5]))

    def test_two_elements(self):
        self.assertEqual(find_runner_up([10, 20]), 10)

    def test_single_element(self):
        self.assertIsNone(find_runner_up([42]))

if __name__ == "__main__":
    unittest.main()