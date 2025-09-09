from util import calculate_average

def main():
    n = int(input("Enter number of students: ").strip())
    student_marks = {}

    for _ in range(n):
        data = input("Enter a name and marks: ").split()
        name = data[0]
        scores = list(map(float, data[1:]))  # convert marks to float
        student_marks[name] = scores

    query_name = input("Enter a name to get average: ").strip()

    if query_name in student_marks:
        result = calculate_average(student_marks[query_name])
        print(f"{result:.2f}")
    else:
        print("Name not found!")

if __name__ == "__main__":
    main()
