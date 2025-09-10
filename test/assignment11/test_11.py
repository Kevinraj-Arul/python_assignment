import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/assignment11")))

from util import compute_determinant

class TestDeterminant(unittest.TestCase):
    def test_sample_case(self):
        matrix = [[1.1, 1.1],
                  [1.1, 1.1]]
        self.assertEqual(compute_determinant(matrix), 0.0)

    def test_identity_matrix(self):
        matrix = [[1, 0],
                  [0, 1]]
        self.assertEqual(compute_determinant(matrix), 1.0)

    def test_negative_values(self):
        matrix = [[-1, -2],
                  [-3, -4]]
        # Determinant = (-1 * -4) - (-2 * -3) = 4 - 6 = -2
        self.assertEqual(compute_determinant(matrix), -2.0)

    def test_non_square_matrix(self):
        with self.assertRaises(ValueError):
            compute_determinant([[1, 2, 3], [4, 5, 6]])

if __name__ == "__main__":
    unittest.main()