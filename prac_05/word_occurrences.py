"""CP1404 Practical
Program to count word occurrences in a string
Estimated time to complete: 30 minutes
"""
def main():
    """Prompt the user for text and display each word with its occurrence count."""
    text = input("Text: ")
    word_counts = count_words(text)
    display_word_counts(word_counts)


def count_words(text):
    """Return a dictionary containing word:count pairs from the given text."""
    words = text.split()
    word_to_count = {}
    for word in words:
        word_to_count[word] = word_to_count.get(word, 0) + 1
    return word_to_count


def display_word_counts(word_to_count):
    """Display words and their counts, sorted alphabetically and formatted neatly."""
    max_length = max(len(word) for word in word_to_count)
    for word, count in sorted(word_to_count.items()):
        print(f"{word:{max_length}} : {count}")


if __name__ == "__main__":
    main()