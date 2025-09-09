import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/Percentage")))
from util import calculate_average

class Test_Util(unittest.TestCase):
    def test_average_integers(self):
        self.assertEqual(calculate_average("alpha",67, 68, 69), 68.00)

    def test_average_floats(self):
        self.assertAlmostEqual(calculate_average("beta",25, 26.5, 28), 26.50)

    def test_average_single_value(self):
        self.assertEqual(calculate_average("raja",100, 101, 102), 101.00)

    def test_average_mixed_values(self):
        self.assertEqual(calculate_average("null",10, 20, 30), 20.00)

if __name__ == "__main__":
    unittest.main()