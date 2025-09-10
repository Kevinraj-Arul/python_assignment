import unittest
import sys
import os

# Add src path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/assignment8")))

from util import calculate_average_marks

class TestCalculateAverageMarks(unittest.TestCase):
    def test_sample_case1(self):
        n = 5
        columns = ["ID", "MARKS", "NAME", "CLASS"]
        rows = [
            ["1", "97", "Raymond", "7"],
            ["2", "50", "Steven", "4"],
            ["3", "91", "Adrian", "9"],
            ["4", "72", "Stewart", "5"],
            ["5", "80", "Peter", "6"],
        ]
        self.assertEqual(calculate_average_marks(n, columns, rows), 78.00)

    def test_sample_case2(self):
        n = 5
        columns = ["MARKS", "CLASS", "NAME", "ID"]
        rows = [
            ["92", "2", "Calum", "1"],
            ["82", "5", "Scott", "2"],
            ["94", "2", "Jason", "3"],
            ["55", "8", "Glenn", "4"],
            ["82", "2", "Fergus", "5"],
        ]
        self.assertEqual(calculate_average_marks(n, columns, rows), 81.00)

    def test_single_student(self):
        n = 1
        columns = ["NAME", "CLASS", "ID", "MARKS"]
        rows = [["Alice", "10", "1", "99"]]
        self.assertEqual(calculate_average_marks(n, columns, rows), 99.00)

    def test_invalid_column_order(self):
        n = 2
        columns = ["NAME", "MARKS", "ID", "CLASS"]
        rows = [["Bob", "70", "1", "9"], ["Tom", "90", "2", "10"]]
        self.assertEqual(calculate_average_marks(n, columns, rows), 80.00)

if __name__ == "__main__":
    unittest.main()