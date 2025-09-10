from util import can_pile

def main():
    t = int(input("Enter number of test cases: ").strip())
    for case in range(t):
        n = int(input(f"\nEnter number of cubes for test case {case+1}: ").strip())
        cubes = list(map(int, input("Enter cube side lengths: ").split()))

        result = can_pile(cubes)
        print(result)

if __name__ == "__main__":
    main()