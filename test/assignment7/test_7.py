import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/assignment7")))
from util import find_day

from util import find_day

class TestFindDay(unittest.TestCase):
    def test_sample_case(self):
        self.assertEqual(find_day(8, 5, 2015), "WEDNESDAY")

    def test_another_date(self):
        self.assertEqual(find_day(1, 1, 2000), "SATURDAY")

    def test_leap_year(self):
        self.assertEqual(find_day(2, 29, 2016), "MONDAY")

    def test_invalid_date(self):
        with self.assertRaises(ValueError):
            find_day(2, 30, 2019)  # Invalid Feb date

if __name__ == "__main__":
    unittest.main()