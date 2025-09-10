def calculate_mean(matrix, axis=1):
    """Compute mean along given axis (0=columns, 1=rows, None=flattened)."""
    if axis == 1:  # row-wise
        means = []
        for row in matrix:
            total = 0
            count = 0
            for val in row:
                total += val
                count += 1
            means.append(total / count)
        return means

    elif axis == 0:  # column-wise
        cols = len(matrix[0])
        means = []
        for j in range(cols):
            total = 0
            count = 0
            for i in range(len(matrix)):
                total += matrix[i][j]
                count += 1
            means.append(total / count)
        return means

    elif axis is None:  # flattened
        total = 0
        count = 0
        for row in matrix:
            for val in row:
                total += val
                count += 1
        return total / count


def calculate_variance(matrix, axis=1):
    """Compute variance along given axis (0=columns, 1=rows, None=flattened)."""
    if axis == 1:  # row-wise
        variances = []
        for row in matrix:
            mean = calculate_mean([row], axis=1)[0]
            total = 0
            count = 0
            for val in row:
                total += (val - mean) ** 2
                count += 1
            variances.append(total / count)
        return variances

    elif axis == 0:  # column-wise
        cols = len(matrix[0])
        variances = []
        means = calculate_mean(matrix, axis=0)
        for j in range(cols):
            total = 0
            count = 0
            for i in range(len(matrix)):
                total += (matrix[i][j] - means[j]) ** 2
                count += 1
            variances.append(total / count)
        return variances

    elif axis is None:  # flattened
        mean = calculate_mean(matrix, axis=None)
        total = 0
        count = 0
        for row in matrix:
            for val in row:
                total += (val - mean) ** 2
                count += 1
        return total / count


def calculate_std(matrix, axis=1):
    """Compute standard deviation along given axis (0=columns, 1=rows, None=flattened)."""
    variance = calculate_variance(matrix, axis)
    if isinstance(variance, list):
        stds = []
        for v in variance:
            stds.append(v ** 0.5)
        return stds
    else:
        return variance ** 0.5