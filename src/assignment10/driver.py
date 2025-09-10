from util import min_max_operation

def main():
    # Read dimensions
    n, m = map(int, input("Enter number of rows and columns: ").split())

    # Read the matrix
    arr = []
    for i in range(n):
        row = list(map(int, input(f"Enter row {i+1} with {m} integers: ").split()))
        if len(row) != m:
            raise ValueError(f"Expected {m} integers in row {i+1}, got {len(row)}")
        arr.append(row)

    # Compute result
    result = min_max_operation(arr)
    print(result)

if __name__ == "__main__":
    main()
