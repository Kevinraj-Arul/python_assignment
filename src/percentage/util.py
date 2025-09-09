def calculate_average(name,*marks):
    if not marks:
        return 0.0
    return sum(marks) / len(marks)
