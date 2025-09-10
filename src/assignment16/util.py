def can_pile(cubes):
    left = 0
    right = len(cubes) - 1
    current = max(cubes[left], cubes[right])  # pick the larger edge first

    while left <= right:
        if cubes[left] >= cubes[right]:
            pick = cubes[left]
            left += 1
        else:
            pick = cubes[right]
            right -= 1

        if pick > current:
            return "No"
        current = pick

    return "Yes"

