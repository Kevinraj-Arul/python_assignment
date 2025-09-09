from util import merge_the_tools

def main():
    s = input("Enter the string: ").strip()
    k = int(input("Enter k (substring size): ").strip())

    result = merge_the_tools(s, k)
    for item in result:
        print(item)

if __name__ == "__main__":
    main()