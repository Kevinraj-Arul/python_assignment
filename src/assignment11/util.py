def compute_determinant(matrix):
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("Input must be a non-empty square matrix")

    # Base case: 1x1 matrix
    if n == 1:
        return round(matrix[0][0], 2)

    # Base case: 2x2 matrix
    if n == 2:
        det_val = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        return round(det_val, 2)

    # Recursive case: expand along first row
    det_val = 0
    for col in range(n):
        # Create minor matrix by removing first row and current column
        minor = []
        for i in range(1, n):
            row = []
            for j in range(n):
                if j != col:
                    row.append(matrix[i][j])
            minor.append(row)

        det_val += ((-1) ** col) * matrix[0][col] * compute_determinant(minor)

    return round(det_val, 2)
