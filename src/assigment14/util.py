def calculate_happiness(arr, like_set, dislike_set):
    happiness = 0
    for val in arr:
        if val in like_set:
            happiness += 1
        elif val in dislike_set:
            happiness -= 1
    return happiness