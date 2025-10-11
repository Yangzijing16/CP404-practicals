def number_stats():
    """Prompt user for 5 numbers and display statistics about them."""
    numbers = []
    for i in range(5):
        number = float(input("Number: "))  # Use float to handle decimal inputs
        numbers.append(number)

    # Output statistics
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


def check_username():
    """Check if the entered username is in the authorized list."""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
                 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    username = input("Enter your username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


def main():
    """Main function to run both exercises."""
    print("Enter 5 numbers:")
    number_stats()
    print("\nWoefully inadequate security checker")
    check_username()


main()