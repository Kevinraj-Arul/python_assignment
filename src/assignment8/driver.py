from util import calculate_average_marks

def main():
    n = int(input("Enter a number of student:").strip())
    columns = input("enter a column names:").split()
    rows = [input("enter student data").split() for _ in range(n)]
    avg = calculate_average_marks(n, columns, rows)
    print(f"{avg:.2f}")

if __name__ == "__main__":
    main()