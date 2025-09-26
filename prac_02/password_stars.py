"""
Password Stars Program
Ask the user for a password, validate it, and print stars equal to its length.
"""

MIN_LENGTH = 6


def main():
    """Run the password stars program."""
    password = get_password()
    print_stars(password)


def get_password():
    """Get a valid password from the user (must meet minimum length)."""
    password = input("Enter password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password too short, must be at least {MIN_LENGTH} characters")
        password = input("Enter password: ")
    return password


def print_stars(password):
    """Print stars equal to the length of the password."""
    print("*" * len(password))


main()
