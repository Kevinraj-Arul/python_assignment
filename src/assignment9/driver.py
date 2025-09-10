from util import floor_array, ceil_array, rint_array

def main():
    arr = input("Enter space-separated floats: ").split()
    arr = [float(x) for x in arr]

    print(floor_array(arr))
    print(ceil_array(arr))
    print(rint_array(arr))

if __name__ == "__main__":
    main()