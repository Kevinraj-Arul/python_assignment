import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/assignmant15")))
from util import  count_word_occurrences


class TestWordCountUtil(unittest.TestCase):
    def test_sample_case(self):
        words = ["bcdef", "abcdefg", "bcde", "bcdef"]
        distinct_count, occurrences = count_word_occurrences(words)
        self.assertEqual(distinct_count, 3)
        self.assertEqual(occurrences, [2, 1, 1])

    def test_all_unique(self):
        words = ["a", "b", "c", "d"]
        distinct_count, occurrences = count_word_occurrences(words)
        self.assertEqual(distinct_count, 4)
        self.assertEqual(occurrences, [1, 1, 1, 1])

    def test_all_same(self):
        words = ["hello", "hello", "hello"]
        distinct_count, occurrences = count_word_occurrences(words)
        self.assertEqual(distinct_count, 1)
        self.assertEqual(occurrences, [3])

    def test_mixed_case(self):
        words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
        distinct_count, occurrences = count_word_occurrences(words)
        self.assertEqual(distinct_count, 3)
        self.assertEqual(occurrences, [3, 2, 1])

if __name__ == "__main__":
    unittest.main()