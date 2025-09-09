from util import find_runner_up

def main():
    n = int(input("Enter the number of participants: "))  # number of participants
    raw_scores = input("Enter the participant's score: ").split()

    # Convert input strings to integers manually
    scores = []
    for value in raw_scores:
        scores.append(int(value))

    result = find_runner_up(scores)
    if result is not None:
        print(result)
    else:
        print("No runner-up found")

if __name__ == "__main__":
    main()