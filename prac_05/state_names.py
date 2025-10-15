"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
def main():
    """Display full state names based on short codes using dictionary lookup."""
    state_code = input("Enter short state: ").upper()  # Accept lowercase too
    while state_code != "":
        try:
            print(f"{state_code} is {CODE_TO_NAME[state_code]}")
        except KeyError:
            print("Invalid short state")
        state_code = input("Enter short state: ").upper()

    print("\nAll states and their names:")
    for code, name in CODE_TO_NAME.items():
        print(f"{code:3} is {name}")


if __name__ == "__main__":
    main()