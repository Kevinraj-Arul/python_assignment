import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/assignment18")))
from util import is_valid_email, filter_emails

class TestEmailUtil(unittest.TestCase):
    def test_valid_emails(self):
        self.assertTrue(is_valid_email("lara@hackerrank.com"))
        self.assertTrue(is_valid_email("brian-23@hackerrank.com"))
        self.assertTrue(is_valid_email("britts_54@hackerrank.com"))

    def test_invalid_missing_at(self):
        self.assertFalse(is_valid_email("lara.hackerrank.com"))
    def test_invalid_website_chars(self):
        self.assertFalse(is_valid_email("lara@hacker#rank.com"))

    def test_invalid_extension_length(self):
        self.assertFalse(is_valid_email("lara@hackerrank.comm"))

    def test_filter_and_sort(self):
        emails = [
            "lara@hackerrank.com",
            "brian-23@hackerrank.com",
            "invalid@com",
            "britts_54@hackerrank.com",
        ]
        result = filter_emails(emails)
        expected = [
            "brian-23@hackerrank.com",
            "britts_54@hackerrank.com",
            "lara@hackerrank.com"
        ]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()