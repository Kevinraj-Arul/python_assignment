from util import print_formatted

def main():
    n = int(input("Enter an integer: ").strip())
    lines = print_formatted(n)
    for line in lines:
        print(line)

if __name__ == "__main__":
    main()