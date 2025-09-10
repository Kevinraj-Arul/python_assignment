import math

def floor_array(arr):
    """Return a list containing the floor of each element in arr."""
    result = []
    for x in arr:
        result.append(math.floor(x))
    return result

def ceil_array(arr):
    """Return a list containing the ceiling of each element in arr."""
    result = []
    for x in arr:
        result.append(math.ceil(x))
    return result

def rint_array(arr):
    """Return a list containing the nearest integer (round) of each element in arr."""
    result = []
    for x in arr:
        result.append(round(x))
    return result