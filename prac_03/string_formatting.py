"""
CP1404/CP5632 - Practical3
String formatting examples and exercises
"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.9

#Produce the output: 1922 Gibson L-5 CES for about $16,036!
print(f"{year} {name} for about ${cost:,.0f}!")

#Produce right-aligned powers of 2 using a for loop and range
for i in range(11):
    result = 2 ** i
    print(f"2 ^ {i:2} is {result:4}")