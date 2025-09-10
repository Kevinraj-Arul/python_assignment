from util import calculate_mean, calculate_variance, calculate_std

def main():
    # Input
    first_line = input("print the first mean value").split()
    x = int(first_line[0])
    y = int(first_line[1])

    matrix = []
    for _ in range(x):
        row_str = input("print the second mean value").split()
        row = []
        for val in row_str:
            row.append(int(val))
        matrix.append(row)

    # Output like NumPy’s behavior
    print(calculate_mean(matrix, axis=1))     # mean along rows
    print(calculate_variance(matrix, axis=0)) # variance along columns
    print(calculate_std(matrix, axis=None))   # std of flattened array

if __name__ == "__main__":
    main()