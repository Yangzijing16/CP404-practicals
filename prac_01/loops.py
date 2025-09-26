# a. Odd numbers 1–20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# b. Count in 10s to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# c. Countdown 20 → 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# d. Print stars on one line
number_of_stars = int(input("Number of stars: "))
print("*" * number_of_stars)

# e. Print lines of increasing stars
number_of_lines = int(input("Number of lines: "))
for i in range(1, number_of_lines + 1):
    print("*" * i)
