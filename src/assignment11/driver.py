from util import compute_determinant

def main():
    # Read size
    n = int(input("Enter size of square matrix: "))

    # Read matrix (without using map)
    matrix = []
    for i in range(n):
        row_input = input(f"Enter row {i+1} with {n} numbers: ").split()
        row = []
        for val in row_input:
            row.append(float(val))   # explicit loop, no map()
        if len(row) != n:
            raise ValueError(f"Expected {n} numbers in row {i+1}, got {len(row)}")
        matrix.append(row)

    # Compute determinant
    result = compute_determinant(matrix)
    print(result)

if __name__ == "__main__":
    main()