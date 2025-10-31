FILENAME = "wimbledon.csv"


def main():
    """Read Wimbledon data file and display champion statistics."""
    records = load_data(FILENAME)
    champions, countries = process_data(records)
    display_results(champions, countries)


def load_data(filename):
    """Read CSV file and return a list of (champion, country) tuples."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # Skip header line
        records = [line.strip().split(",")[1:3] for line in in_file]
    return records


def process_data(records):
    """Return a dictionary of champion: wins and a set of countries."""
    champions = {}
    countries = set()
    for country, champion in records:
        champions[champion] = champions.get(champion, 0) + 1
        countries.add(country)
    return champions, countries


def display_results(champions, countries):
    """Display champions with their win counts and list of countries."""
    print("Wimbledon Champions:")
    for champion, wins in champions.items():
        print(f"{champion} {wins}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


if __name__ == "__main__":
    main()