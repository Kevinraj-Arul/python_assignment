from util import count_word_occurrences

def main():
    # Read number of words
    n = int(input("Enter number of words: ").strip())

    # Read words
    words = []
    for i in range(n):
        word = input(f"Enter word {i+1}: ").strip()
        words.append(word)

    # Process
    distinct_count, occurrences = count_word_occurrences(words)

    # Output
    print("\nOutput:")
    print(distinct_count)
    print(" ".join(str(x) for x in occurrences))

if __name__ == "__main__":
    main()