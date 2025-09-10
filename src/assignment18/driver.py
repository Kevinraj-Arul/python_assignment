
from util import filter_emails
def main():
    n = int(input("Enter number of emails: ").strip())
    emails = []
    for i in range(n):
        email = input(f"Enter email {i+1}: ").strip()
        emails.append(email)

    result = filter_emails(emails)
    print(result)

if __name__ == "__main__":
    main()