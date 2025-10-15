# Constant dictionary mapping colour names to hex codes
COLOUR_TO_CODE = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "black": "#000000",
    "blueviolet": "#8a2be2",
    "brown": "#a52a2a",
    "chartreuse": "#7fff00",
    "coral": "#ff7f50",
    "crimson": "#dc143c",
    "darkgreen": "#006400"
}


def main():
    """Look up hex colour codes by name."""
    colour_name = input("Enter a colour name: ").strip().lower()
    while colour_name != "":
        try:
            print(f"{colour_name} = {COLOUR_TO_CODE[colour_name]}")
        except KeyError:
            print("Invalid colour name")
        colour_name = input("Enter a colour name: ").strip().lower()


if __name__ == "__main__":
    main()