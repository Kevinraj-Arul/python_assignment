from util import calculate_happiness

def main():
    # Read n, m
    first_line = input("Enter n and m: ").split()
    n = int(first_line[0])
    m = int(first_line[1])

    # Read array
    arr_line = input("Enter array elements: ").split()
    arr = []
    for i in range(n):
        arr.append(int(arr_line[i]))

    # Read like set
    like_line = input("Enter like set elements: ").split()
    like_set = set()
    for i in range(m):
        like_set.add(int(like_line[i]))

    # Read dislike set
    dislike_line = input("Enter dislike set elements: ").split()
    dislike_set = set()
    for i in range(m):
        dislike_set.add(int(dislike_line[i]))

    # Compute result
    result = calculate_happiness(arr, like_set, dislike_set)
    print("Final Happiness:", result)

if __name__ == "__main__":
    main()