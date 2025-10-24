def main():
    """Prompt the user for email addresses and display names with confirmation."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation == "n" or confirmation == "no":
            name = input("Name: ").strip()
        email_to_name[email] = name
        email = input("Email: ")

    display_email_mappings(email_to_name)


def get_name_from_email(email):
    """Extract a name guess from the given email address."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


def display_email_mappings(email_to_name):
    """Display all collected email-name pairs."""
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()