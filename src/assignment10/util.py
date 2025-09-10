def min_max_operation(arr):
    if not arr or not arr[0]:
        raise ValueError("Input array cannot be empty")

    row_mins = [min(row) for row in arr]
    return max(row_mins)