from util import find_day

def main():
    month, day, year = map(int, input("Enter date (MM DD YYYY): ").split())
    print(find_day(month, day, year))

if __name__ == "__main__":
    main()