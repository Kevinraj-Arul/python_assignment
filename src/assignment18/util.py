def is_valid_email(email):
    if "@" not in email or "." not in email:
        return False

    try:
        username, rest = email.split("@")
        website, extension = rest.split(".")
    except ValueError:
        return False

    # username validation
    for ch in username:
        if not (ch.isalnum() or ch in "-_"):
            return False

    # website validation
    for ch in website:
        if not ch.isalnum():
            return False

    # extension validation
    if not extension.isalpha() or len(extension) > 3:
        return False

    return True


def filter_emails(emails):
    valid = []
    for email in emails:
        if is_valid_email(email):
            valid.append(email)
    valid.sort()
    return valid