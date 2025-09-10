import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/assignment17")))
from util import probability_of_a

class TestProbabilityOfA(unittest.TestCase):
    def test_sample_case(self):
        letters = ["a", "a", "c", "d"]
        k = 2
        result = probability_of_a(letters, k)
        self.assertAlmostEqual(result, 0.8333, places=4)

    def test_all_a(self):
        letters = ["a", "a", "a", "a"]
        k = 2
        result = probability_of_a(letters, k)
        self.assertAlmostEqual(result, 1.0000, places=4)

    def test_no_a(self):
        letters = ["b", "c", "d", "e"]
        k = 2
        result = probability_of_a(letters, k)
        self.assertAlmostEqual(result, 0.0000, places=4)

    def test_single_a(self):
        letters = ["a", "b", "c", "d"]
        k = 1
        result = probability_of_a(letters, k)
        self.assertAlmostEqual(result, 0.2500, places=4)

    def test_large_case(self):
        letters = ["a", "b", "c", "a", "d", "e"]
        k = 3
        result = probability_of_a(letters, k)
        # Expected calculation: total = 20, no_a = 4C3 = 4, prob = 1 - 4/20 = 0.8
        self.assertAlmostEqual(result, 0.8000, places=4)

if __name__ == "__main__":
    unittest.main()