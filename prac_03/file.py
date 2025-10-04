"""
CP1404/CP5632 - Practical
"""

# 1. Write name to file using open() and close()
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()



# 2. Read name from file and print greeting
in_file = open("name.txt", "r")
name = in_file.read().strip()  # remove newline
in_file.close()
print(f"Hi {name}!")


# 3. Read first two numbers, add them, print result
with open("numbers.txt", "r") as numbers_file:
    number1 = int(numbers_file.readline())
    number2 = int(numbers_file.readline())
    result = number1 + number2
print(result)



# 4. Print the total for all lines in numbers.txt
total = 0
with open("numbers.txt", "r") as numbers_file:
    for line in numbers_file:
        total += int(line)
print(total)
