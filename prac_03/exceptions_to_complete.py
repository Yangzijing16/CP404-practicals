"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True   # this line means the input was valid, so we can stop the loop
    except ValueError:       # catch the correct exception for invalid integer conversion
        print("Please enter a valid integer.")

print("Valid result is:", result)
