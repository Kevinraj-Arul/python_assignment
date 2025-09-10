import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/assignment12")))

from util import calculate_mean, calculate_variance, calculate_std

class TestStatsTools(unittest.TestCase):
    def setUp(self):
        self.matrix = [
            [1, 2],
            [3, 4]
        ]

    def test_mean_row(self):
        result = calculate_mean(self.matrix, axis=1)
        expected = [1.5, 3.5]
        for i in range(len(result)):
            self.assertAlmostEqual(result[i], expected[i], places=6)


    def test_variance_col(self):
        result = calculate_variance(self.matrix, axis=0)
        expected = [1.0, 1.0]
        for i in range(len(result)):
            self.assertAlmostEqual(result[i], expected[i], places=6)

    def test_variance_flat(self):
        result = calculate_variance(self.matrix, axis=None)
        expected = 1.25
        self.assertAlmostEqual(result, expected, places=6)

    def test_std_row(self):
        result = calculate_std(self.matrix, axis=1)
        expected = [0.5, 0.5]
        for i in range(len(result)):
            self.assertAlmostEqual(result[i], expected[i], places=6)

    def test_std_col(self):
        result = calculate_std(self.matrix, axis=0)
        expected = [1.0, 1.0]
        for i in range(len(result)):
            self.assertAlmostEqual(result[i], expected[i], places=6)


if __name__ == "__main__":
    unittest.main()