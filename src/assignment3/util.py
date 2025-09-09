def mutate_string(string, position, character):
    if position < 0 or position >= len(string):
        raise ValueError("Position out of range")
    return string[:position] + character + string[position+1:]