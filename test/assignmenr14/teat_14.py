import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/assigment14")))
from util import calculate_happiness

class TestHappinessUtil(unittest.TestCase):
    def test_sample_case(self):
        arr = [1, 5, 3]
        like_set = {3, 1}
        dislike_set = {5, 7}
        self.assertEqual(calculate_happiness(arr, like_set, dislike_set), 1)

    def test_all_likes(self):
        arr = [1, 2, 3]
        like_set = {1, 2, 3}
        dislike_set = {4, 5}
        self.assertEqual(calculate_happiness(arr, like_set, dislike_set), 3)

    def test_all_dislikes(self):
        arr = [4, 5, 6]
        like_set = {1, 2}
        dislike_set = {4, 5, 6}
        self.assertEqual(calculate_happiness(arr, like_set, dislike_set), -3)

    def test_no_effect(self):
        arr = [8, 9, 10]
        like_set = {1, 2}
        dislike_set = {3, 4}
        self.assertEqual(calculate_happiness(arr, like_set, dislike_set), 0)

    def test_mixed_case(self):
        arr = [1, 2, 3, 4, 5]
        like_set = {1, 2}
        dislike_set = {4, 5}
        # +1 for 1, +1 for 2, -1 for 4, -1 for 5 = 0
        self.assertEqual(calculate_happiness(arr, like_set, dislike_set), 0)

if __name__ == "__main__":
    unittest.main()