# Program Name: Assignment2.py
# Course: IT3883/Section W01
# Student Name: Olu Lamodi
# Assignment Number: Assignment 2
# Due Date: 06/19/2026
# Purpose: This program reads student names and test scores from an input file,
#          calculates the average score for each student, and displays the results
#          in descending order by average grade.
# Resources: No external resources used - all code written independently.

# Ask user for the input file name
input_file = input("Enter the input file name: ")

# Create empty list to store student records
student_records = []

# Open and read the file
data_file = open(input_file, 'r')

# Process each line in the file
for record in data_file:
    # Split each line into separate pieces
    items = record.split()

    # First item is the student's name
    student_name = items[0]

    # Next 6 items are test scores - convert to numbers
    test1 = float(items[1])
    test2 = float(items[2])
    test3 = float(items[3])
    test4 = float(items[4])
    test5 = float(items[5])
    test6 = float(items[6])

    # Add up all test scores
    total_score = test1 + test2 + test3 + test4 + test5 + test6

    # Calculate average by dividing total by number of tests
    grade_average = total_score / 6

    # Store the student name and average in our list
    student_records.append([student_name, grade_average])

# Done reading file, so close it
data_file.close()

# Sort students by average from highest to lowest using bubble sort
for position in range(len(student_records)):
    for next_position in range(position + 1, len(student_records)):
        # Compare current student average with next student average
        if student_records[position][1] < student_records[next_position][1]:
            # Swap positions if current average is lower
            temporary = student_records[position]
            student_records[position] = student_records[next_position]
            student_records[next_position] = temporary

# Display the sorted results
for entry in student_records:
    # Print student name and average with 2 decimal places
    print(entry[0], format(entry[1], '.2f'))
