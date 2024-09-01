# List of maximum points available for each assignment type
max_points = [25, 25, 50, 25, 100]

# List of assignment names
assignments = ['hw1', 'hw2', 'quiz', 'hw3', 'test']

# Dictionary to store student names and their grades, initialized with a sample
students = {'Max': max_points}

# Function to display the menu options
def print_menu():
    print("1. Add student")
    print("2. Remove student")
    print("3. Print grades")
    print("4. Record grade")
    print("5. Print Menu")
    print("6. Exit")

# Function to print all grades for all students
def print_all_grades():
    print('\t', '\t', end=' ')
    # Print assignment names in a tabulated format
    for i in range(len(assignments)):
        print(assignments[i], '\t', '\t', end=' ')
    print()  # New line after printing all assignment names

    # Sort and print each student's grades
    keys = list(students.keys())
    keys.sort()
    for x in keys:
        print(x, '\t', end=' ')
        grades = students[x]
        print_grades(grades)  # Call to function to print grades of a single student

# Helper function to print grades for a single student
def print_grades(grades):
    for i in range(len(grades)):
        print(grades[i], '\t', '\t', end=' ')
    print()  # New line after grades

# Display the menu at the start
print_menu()
menu_choice = 0  # Variable to store the user's menu choice

# Continue the program until the user chooses to exit (option 6)
while menu_choice != 6:
    menu_choice = int(input("Menu Choice (1-6): "))
    if menu_choice == 1:
        # Add a new student with grades initialized to zeros based on the number of assignments
        name = input("Student to add: ")
        students[name] = [0] * len(max_points)
    elif menu_choice == 2:
        # Remove an existing student
        name = input("Student to remove: ")
        if name in students:
            del students[name]
        else:
            print("Student:", name, "not found")
    elif menu_choice == 3:
        # Print all grades
        print_all_grades()
    elif menu_choice == 4:
        # Record a grade for a student
        print("Record Grade")
        name = input("Student: ")
        if name in students:
            grades = students[name]
            print("Type in the number of the grade to record")
            print("Type a 0 (zero) to exit")
            # Display all assignment names with indices for user to select
            for i in range(len(assignments)):
                print(i + 1, assignments[i], '\t', end=' ')
            print()  # New line
            which = 1234  # Initial dummy value to enter the loop
            while which != -1:
                which = int(input("Change which Grade: "))
                if 0 <= which < len(grades):
                    # Record new grade after validating the index
                    grade = int(input("Grade: "))
                    grades[which] = grade
                elif which != -1:
                    print("Invalid Grade Number")
        else:
            print("Student not found")
    elif menu_choice != 6:
        # Reprint the menu unless exiting
        print_menu()
