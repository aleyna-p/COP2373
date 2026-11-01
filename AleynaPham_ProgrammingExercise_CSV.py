"""
File: AleynaPham_ProgrammingExercise_CSV.py
Description: Program prompts instructor to enter student names and three
             exam grades, saves data into a grades.csv file using csv
             module, then reads and displays data in tabular format.
"""

import csv

def save_grades_to_csv():
    """
    Prompts instructor for number of students, collects their first
    name, last name, and three exam grades as integers, then
    records data to grades.csv.

    Parameters:
        None.

    Variables:
        num_students (int): Number of students instructor inputs.
        file_name (str): Name of CSV file.
        header (list): Column headers for CSV file.
        student_data (list): List containing student's info.

    Logic:
        1. Prompt instructor number of students to enter.
        2. Open grades.csv in write mode using with keyword.
        3. Write column header row.
        4. Loop through number of students to retrieve names and exam scores.
        5. Write each student record into CSV file.

    Return:
        None.
    """
    num_students = int(input("Please enter the number of students: "))
    file_name = "grades.csv"

    # Header row.
    header = ["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"]

    # Open file then write data using with keyword.
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for i in range(num_students):
            print(f"\nDetails for student {i + 1}:")
            first_name = input("\nFirst name: ")
            last_name = input("Last name: ")
            exam1 = int(input("Exam 1 grade: "))
            exam2 = int(input("Exam 2 grade: "))
            exam3 = int(input("Exam 3 grade: "))

            # Compile student data into list
            student_data = [first_name, last_name, exam1, exam2, exam3]
            writer.writerow(student_data)

    print(f"\nData has been written to {file_name}!")


def display_grades():
    """
    Reads grades.csv file and displays student data in tabular format.

    Parameters:
        None.

    Variables:
        file_name (str): Name of the CSV file to read ("grades.csv").

    Logic:
        1. Open grades.csv in read mode using with keyword.
        2. Use csv.reader to read rows from file.
        3. Loop through each row and print in tabular format.

    Return:
        None.
    """
    file_name = "grades.csv"

    print("\n⋆✴︎˚｡ Student Grades ｡˚✴︎⋆")

    # Open file and read data using with keyword.
    with open(file_name, mode="r") as file:
        reader = csv.reader(file)

        # Loop through each row and print in tabular format.
        for row in reader:
            print(f"\n{row[0]:<15} {row[1]:<15} {row[2]:<10} {row[3]:<10} {row[4]:<10}")


def main():
    """
    Main function running program.

    Parameters:
        None.

    Variables:
        None.

    Logic:
        1. Print program header.
        2. Call save_grades_to_csv function to create and populate file.
        3. Call display_grades function to read and display table.

    Return:
        None.
    """
    print("\n────────────────────────────────────────")
    print("      ⋆✴︎˚｡ Grade Management ｡˚✴︎⋆")
    print("────────────────────────────────────────")

    # Save grades to CSV file.
    save_grades_to_csv()

    # Read and display grades in tabular format.
    display_grades()

# Run main function.
if __name__ == "__main__":
    main()