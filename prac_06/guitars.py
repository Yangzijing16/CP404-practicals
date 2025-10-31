"""Program to store and display details of guitars using the Guitar class."""

from guitar import Guitar


def main():
    """Store user guitars and display their details."""
    guitars = []

    print("My guitars!")
    name = input("Name: ")

    # Continue while the user provides a name
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:,.2f} added.\n")

        # Ask again for the next guitar
        name = input("Name: ")

    if not guitars:
        print("No guitars entered.")
        return

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ == "__main__":
    main()
