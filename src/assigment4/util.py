def merge_the_tools(string, k):
    if k <= 0 or len(string) % k != 0:
        raise ValueError("k must be a positive divisor of string length")

    result = []
    for i in range(0, len(string), k):
        substring = string[i:i+k]
        seen = set()
        unique = ""
        for char in substring:
            if char not in seen:
                seen.add(char)
                unique += char
        result.append(unique)
    return result