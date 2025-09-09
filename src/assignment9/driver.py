from util import time_delta

def main():
    t = int(input("Enter number of test cases: ").strip())
    for _ in range(t):
        t1 = input("Enter first timestamp: ").strip()
        t2 = input("Enter second timestamp: ").strip()
        print(time_delta(t1, t2))

if __name__ == "__main__":
    main()