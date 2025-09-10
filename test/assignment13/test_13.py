import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/assignment13")))
from util import time_difference

class TestTimeDifference(unittest.TestCase):
    def test_same_time_different_zones(self):
        t1 = "Sun 10 May 2015 13:54:36 -0700"
        t2 = "Sun 10 May 2015 13:54:36 -0000"
        self.assertEqual(time_difference(t1, t2), 25200)  # 7 hours

    def test_different_days(self):
        t1 = "Sat 02 May 2015 19:54:36 +0530"
        t2 = "Fri 01 May 2015 13:54:36 -0000"
        self.assertEqual(time_difference(t1, t2), 88200)

    def test_exact_same_time(self):
        t1 = "Mon 01 Jan 2024 00:00:00 +0000"
        t2 = "Mon 01 Jan 2024 00:00:00 +0000"
        self.assertEqual(time_difference(t1, t2), 0)

    def test_half_hour_offset(self):
        t1 = "Mon 01 Jan 2024 12:00:00 +0530"
        t2 = "Mon 01 Jan 2024 06:30:00 +0000"
        self.assertEqual(time_difference(t1, t2), 0)

if __name__ == "__main__":
    unittest.main()
