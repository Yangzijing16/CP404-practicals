DEFAULT_FUEL = 0
DEFAULT_ODOMETER = 0


class Car:
    """Represent a Car object."""

    def __init__(self, name="", fuel=DEFAULT_FUEL):
        """Initialise a Car instance.

        Args:
            name (str): The name of the car.
            fuel (float): The amount of fuel (1 unit = 1 km of driving).
        """
        self.name = name
        self.fuel = fuel
        self._odometer = DEFAULT_ODOMETER

    def add_fuel(self, amount):
        """Add amount to the car's fuel.

        Args:
            amount (float): The amount of fuel to add.
        """
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.

        If the distance is greater than the available fuel,
        the car drives until it runs out of fuel.

        Args:
            distance (float): The distance to drive.

        Returns:
            float: The actual distance driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance

        self._odometer += distance
        return distance

    def __str__(self):
        """Return a string representation of the car."""
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"