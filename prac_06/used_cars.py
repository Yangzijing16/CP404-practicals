"""Demo test code to show how to use the Car class with a named car 'Limo'."""

from prac_06.car import Car

# Constants
INITIAL_FUEL = 100
EXTRA_FUEL = 20
DRIVE_DISTANCE = 115


def main():
    """Demonstrate basic Car class functionality."""
    # Create a new Car object called "Limo" with 100 units of fuel
    limo = Car("Limo", INITIAL_FUEL)

    # Add 20 more units of fuel
    limo.add_fuel(EXTRA_FUEL)

    # Print the amount of fuel
    print(f"{limo.name} fuel after refueling: {limo.fuel}")

    # Attempt to drive 115 km
    distance_driven = limo.drive(DRIVE_DISTANCE)
    print(f"{limo.name} drove {distance_driven} km.")

    # Print the car object to test __str__
    print(limo)


if __name__ == "__main__":
    main()
