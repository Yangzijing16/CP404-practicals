"""
Score Program
Get a user's score, print the result, and generate a random score with its result.
"""

import random


def main():
    """Run the score program."""
    score = get_valid_score()
    print(f"Your score: {score}, Result: {get_score_result(score)}")

    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}, Result: {get_score_result(random_score)}")


def get_valid_score():
    """Prompt the user to enter a valid score (0–100 inclusive)."""
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Must be between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score


def get_score_result(score):
    """Return the result category for a given score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
