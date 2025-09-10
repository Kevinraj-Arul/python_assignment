from util import probability_of_a

def main():
    n = int(input("Enter number of letters: ").strip())
    letters = input("Enter letters separated by space: ").split()
    k = int(input("Enter number of indices to select: ").strip())

    result = probability_of_a(letters, k)
    print(f"{result:.4f}")

if __name__ == "__main__":
    main()