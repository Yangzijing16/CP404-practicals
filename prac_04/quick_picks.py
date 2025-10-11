import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6

def main():
    """Generate random quick pick lines with unique numbers."""
    num_picks = int(input("How many quick picks? "))
    for _ in range(num_picks):
        quick_pick = generate_quick_pick()
        # Format numbers to align neatly (2 spaces for single-digit, 1 for double-digit)
        formatted_pick = [f"{num:2}" for num in quick_pick]
        print(" ".join(formatted_pick))

def generate_quick_pick():
    """Generate one line of 6 unique random numbers, sorted."""
    numbers = []
    while len(numbers) < NUMBERS_PER_LINE:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:  # Ensure no duplicates
            numbers.append(number)
    return sorted(numbers)  # Return sorted list

main()