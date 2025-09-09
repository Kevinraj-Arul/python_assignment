from collections import namedtuple

def calculate_average_marks(n: int, columns: list, rows: list) -> float:
    Student = namedtuple("Student", columns)
    total = sum(int(Student(*row).MARKS) for row in rows)
    return round(total / n, 2)