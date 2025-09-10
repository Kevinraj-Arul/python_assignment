def factorial(n):
    """Compute factorial of n without recursion."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def nCr(n, r):
    """Compute combinations nCr."""
    if r > n:
        return 0
    return factorial(n) // (factorial(r) * factorial(n - r))


def probability_of_a(letters, k):
  
    n = len(letters)
    count_a = 0
    for letter in letters:
        if letter == "a":
            count_a += 1

    # total number of ways
    total_combinations = nCr(n, k)

    # number of ways where NO 'a' is chosen
    non_a = n - count_a
    no_a_combinations = nCr(non_a, k)

    # probability at least one 'a'
    probability = 1 - (no_a_combinations / total_combinations)
    return round(probability, 4)