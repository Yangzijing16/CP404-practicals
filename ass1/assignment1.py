"""
CP1404/CP5632 Assignment 1 - Books to Read 1.0
Name: Yang Zijing
Date: 19/10/2025
GitHub Repo Link: https://github.com/cp1404-students/a1-books-Yangzijing16.git

Description:
A simple program for managing a reading list. It loads book data from a CSV file,
allows users to display, add, and mark books as completed, and then saves updates
back to the file when quitting.
"""
from operator import itemgetter

MENU = (
    "Menu:\n"
    "D - Display books\n"
    "A - Add new book\n"
    "C - Complete a book\n"
    "Q - Quit"
)
BOOKS_FILE = "books.csv"
STATUS_UNREAD = "u"
STATUS_COMPLETED = "c"

# Constants for list indices
TITLE_INDEX = 0
AUTHOR_INDEX = 1
PAGES_INDEX = 2
STATUS_INDEX = 3

def main():
    """Main function to run the Books To Read program."""
    print("Books to Read 1.0 by Yang Zijing")

    # Step 1: Load books from CSV
    books = load_books(BOOKS_FILE)
    print(f"{len(books)} books loaded.")

    # Step 2: Menu loop
    choice = ''
    while choice != "q":
        print(MENU)
        choice = input(">>> ").strip().lower()

        if choice == "d":
            display_books(books)
        elif choice == "a":
            add_book(books)
        elif choice == "c":
            complete_book(books)
        elif choice == "q":
            # Step 3: Save to CSV and exit
            save_books(BOOKS_FILE, books)
            print(f"{len(books)} books saved to {BOOKS_FILE}")
            print('"So many books, so little time. Frank Zappa"')
        else:
            print("Invalid menu choice")


def load_books(filename):
    """Load books from CSV file into a list of lists."""

    books = []
    with open(filename, "r", encoding="utf-8") as in_file:
        for line in in_file:
            title, author, pages, status = line.strip().split(",")
            books.append([title, author, int(pages), status])
    return books

def save_books(filename, books):
    """Save the list of books back to a CSV file."""
    with open(filename, "w", encoding="utf-8") as out_file:
        for book in books:
            print(f"{book[0]},{book[1]},{book[2]},{book[3]}", file=out_file)

def display_books(books):
    """Display all books in a neat, aligned format and show reading summary.
    """
    if not books:
        print("No books found.")
        return

    # Sort by Author (index 1) then Title (index 0)
    # itemgetter is an efficient way to sort by multiple indices
    sorted_books = sorted(books, key=itemgetter(AUTHOR_INDEX, TITLE_INDEX))

    # Determine required column widths for alignment
    title_width = max(len(book[TITLE_INDEX]) for book in sorted_books)
    author_width = max(len(book[AUTHOR_INDEX]) for book in sorted_books)

    unread_books = [book for book in sorted_books if book[STATUS_INDEX] == STATUS_UNREAD]
    total_pages_unread = sum(book[PAGES_INDEX] for book in unread_books)
    num_unread = len(unread_books)

    # Display the list
    for i, book in enumerate(sorted_books, 1):
        status_star = "*" if book[STATUS_INDEX] == STATUS_UNREAD else " "
        print(f"{status_star}{i}. {book[TITLE_INDEX]:<{title_width}} by {book[AUTHOR_INDEX]:<{author_width}} {book[PAGES_INDEX]:>4} pages")

    # Display summary
    if num_unread > 0:
        print(f"You still need to read {total_pages_unread} pages in {num_unread} books.")
    else:
        print("No books left to read. Why not add a new book?")


def add_book(books):
    """Prompt user to add a new unread book to the list."""
    title = get_non_blank_input("Title: ")
    author = get_non_blank_input("Author: ")
    pages = get_positive_int("Number of pages: ")

    books.append([title, author, pages, STATUS_UNREAD])
    print(f"{title} by {author} ({pages} pages) added.")


def complete_book(books):
    """Allow the user to mark an unread book as completed.
    """
    sorted_books = sorted(books, key=itemgetter(AUTHOR_INDEX, TITLE_INDEX))

    unread_number = sum(1 for book in sorted_books if book[STATUS_INDEX] == STATUS_UNREAD)

    if unread_number == 0:
        print("No unread books - well done!")
        return

    # Display the books (must be done to show numbers to the user)
    display_books(books)

    is_valid_book_choice = False
    while not is_valid_book_choice:
        book_number = get_positive_int("Enter the number of a book to mark as completed: ")

        # Check if number is within the valid range
        if 1 <= book_number <= len(sorted_books):
            selected_book = sorted_books[book_number - 1]

            if selected_book[STATUS_INDEX] == STATUS_COMPLETED:
                print("That book is already completed")
            else:
                # Found a valid unread book: update the status
                selected_book[STATUS_INDEX] = STATUS_COMPLETED
                print(f"{selected_book[TITLE_INDEX]} by {selected_book[AUTHOR_INDEX]} completed!")
                is_valid_book_choice = True
        else:
            print("Invalid book number")


def get_non_blank_input(prompt):
    """Prompt the user until a non-blank input is entered (reused logic).

    Args:
        prompt (str): The input prompt message.
    Returns:
        str: A valid, non-empty string.
    """
    #While loop until valid input is received
    input_string = input(prompt).strip()
    while not input_string:
        print("Input can not be blank")
        input_string = input(prompt).strip()
    return input_string


def get_positive_int(prompt):
    """Prompt the user until an integer greater than 0 is entered (reused logic).

    Args:
        prompt (str): The input prompt message.
    Returns:
        int: A valid positive integer.
    """
    is_valid = False
    number = 0
    # Loop until a valid, positive integer is entered
    while not is_valid:
        try:
            input_string = input(prompt)
            number = int(input_string)  # Attempt conversion

            if number <= 0:
                # Check for positive number (> 0)
                print("Number must be > 0")
            else:
                is_valid = True
        except ValueError:
            # Catch non-integer input
            print("Invalid input please enter a valid number")
    return number

if __name__ == "__main__":
    main()