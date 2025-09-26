"""
Score Menu Program
This program allows the user to get a valid score, print the result,
show stars, and quit. It demonstrates functions, SRP, and menu handling.
"""

import random


def main():
    """Run the score menu program."""
    score = get_valid_score()
    choice = ""
    while choice.upper() != "Q":
        print_menu()
        choice = input(">>> ").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(f"Result: {determine_result(score)}")
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Farewell! Thanks for using the program.")
        else:
            print("Invalid choice. Please try again.")


def print_menu():
    """Display the main menu options."""
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def get_valid_score():
    """Prompt the user for a valid score (0–100 inclusive)."""
    score = int(input("Enter a score (0-100): "))
    while not is_valid_score(score):
        print("Invalid score. Try again.")
        score = int(input("Enter a score (0-100): "))
    return score


def is_valid_score(score):
    """Check if a score is within the valid range (0–100 inclusive)."""
    return 0 <= score <= 100


def determine_result(score):
    """Determine the result category based on the score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    """Print stars equal to the score value."""
    print("*" * score)


main()
