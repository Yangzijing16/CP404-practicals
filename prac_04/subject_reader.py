"""
CP1404/CP5632 Practical
Data file -> lists program
"""

SUBJECT_FILE = "subject_data.txt"


def main():
    subject_data = get_subjects_data(SUBJECT_FILE)
    display_subject_details(subject_data)


def get_subjects_data(filename=SUBJECT_FILE):
    """Read subject data from file and return as a list of lists."""
    subjects = []
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()  # Remove the \n
            parts = line.split(',')  # Separate the data into parts
            parts[2] = int(parts[2])  # Convert student number to integer
            subjects.append(parts)  # Add the parts list to subjects
    return subjects


def display_subject_details(subjects):
    """Display subject details in a formatted way."""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


main()