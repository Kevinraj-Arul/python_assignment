from util import mutate_string

def main():
    string = input("Enter a string: ")
    position = int(input("Enter the position to modify: "))
    character = input("Enter the new character: ")

    result = mutate_string(string, position, character)
    print(result)

if __name__ == "__main__":
    main()