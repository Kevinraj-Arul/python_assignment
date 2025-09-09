from util import generate_logo

def main():
    thickness = int(input("Enter thickness (odd number): ").strip())
    logo_lines = generate_logo(thickness)
    for line in logo_lines:
        print(line)

if __name__ == "__main__":
    main()