"""Tests for the Guitar class."""

from datetime import datetime
from guitar import Guitar

CURRENT_YEAR = datetime.now().year

# Test guitars
guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Another Guitar", 2013, 1512.90)

# Calculate expected values dynamically
expected_age1 = CURRENT_YEAR - guitar1.year
expected_age2 = CURRENT_YEAR - guitar2.year

print(f"{guitar1.name} get_age() - Expected {expected_age1}. Got {guitar1.get_age()}")
print(f"{guitar2.name} get_age() - Expected {expected_age2}. Got {guitar2.get_age()}")

print(f"{guitar1.name} is_vintage() - Expected {expected_age1 >= 50}. Got {guitar1.is_vintage()}")
print(f"{guitar2.name} is_vintage() - Expected {expected_age2 >= 50}. Got {guitar2.is_vintage()}")
