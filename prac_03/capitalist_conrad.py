"""
CP1404/CP5632 - Practical3
Stock price simulator for a volatile stock.
The price starts at $10.00, with a 50% chance each day to increase by 0 to 17.5%
or decrease by 0 to 5%. The program ends if the price falls below $1.00 or rises
above $100.00. Output is written to a file with prices formatted to the nearest cent.
"""

import random

# Constants
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.00
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
FILENAME = "stock_prices.txt"

# Initialize variables
price = INITIAL_PRICE
number_of_days = 0

# Open file for writing
try:
    out_file = open(FILENAME, 'w')

    # Print starting price
    print(f"Starting price: ${price:,.2f}", file=out_file)

    # Simulate price changes until price is out of bounds
    while MIN_PRICE <= price <= MAX_PRICE:
        number_of_days += 1
        price_change = 0

        # 50% chance of increase or decrease
        if random.randint(1, 2) == 1:
            # Random increase between 0 and 17.5%
            price_change = random.uniform(0, MAX_INCREASE)
        else:
            # Random decrease between 0 and 5%
            price_change = random.uniform(-MAX_DECREASE, 0)

        # Update price
        price *= (1 + price_change)
        # Write price for the day
        print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

    # Close the file
    out_file.close()

except IOError:
    print("Error writing to file")