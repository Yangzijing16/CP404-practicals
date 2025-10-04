"""
CP1404/CP5632 - Practical
Random number exercises
"""

import random

# What did you see on line 1?
# I saw a random integer between 5 and 20, such as 12, 18, or 7.
# Smallest number: 5
# Largest number: 20

# What did you see on line 2?
# I saw a random integer from the sequence [3, 5, 7, 9], such as 5 or 9.
# Smallest number: 3
# Largest number: 9
# Could line 2 have produced a 4? No, because randrange(3, 10, 2) only produces odd numbers (3, 5, 7, 9) due to the step of 2.

# What did you see on line 3?
# I saw a random float between 2.5 and 5.5, such as 3.827 or 4.231.
# Smallest number: 2.5
# Largest number: 5.5

# Code to produce a random number between 1 and 100 inclusive
print(random.randint(1, 100))