import numpy as np

def compute_determinant(matrix):
    if not matrix or len(matrix) != len(matrix[0]):
        raise ValueError("Input must be a non-empty square matrix")

    det_val = np.linalg.det(np.array(matrix))
    return round(det_val, 2)