# Define a function to display the menu options to the user
def print_menu():
    print('1. Print Phone Numbers')  # Option to print all phone numbers
    print('2. Add a Phone Number')   # Option to add a new phone number
    print('3. Remove a Phone Number')  # Option to remove an existing phone number
    print('4. Lookup a Phone Number')  # Option to find a phone number by name
    print('5. Quit')  # Option to quit the program
    print()  # Print a blank line for better readability

# Initialize an empty dictionary to store name-number pairs
numbers = {
    "Howard" : "17513353052"
}

# Variable to store the user's menu choice
menu_choice = 0

# Display the menu options
print_menu()

# Continue running the program until the user decides to quit (option 5)
while menu_choice != 5:
    # Prompt the user to input a choice and convert it to an integer
    menu_choice = int(input("Type in a number (1-5): "))
    
    # If the choice is 1, print all stored phone numbers
    if menu_choice == 1:
        print("Telephone Numbers:")
        for x in numbers.keys():
            print("Name: ", x, "\tNumber:", numbers[x])
        print()  # Print a blank line for better readability

    # If the choice is 2, allow the user to add a new name-number pair
    elif menu_choice == 2:
        print("Add Name and Number")
        name = input("Name: ")  # Prompt for the name
        phone = input("Number: ")  # Prompt for the phone number
        numbers[name] = phone  # Store the new name-number pair in the dictionary

    # If the choice is 3, allow the user to remove a name-number pair
    elif menu_choice == 3:
        print("Remove Name and Number")
        name = input("Name: ")  # Prompt for the name to be removed
        if name in numbers:  # Check if the name exists in the dictionary
            del numbers[name]  # Remove the name-number pair if found
        else:
            print(name, "was not found")  # Inform the user if the name was not found

    # If the choice is 4, allow the user to lookup a number by name
    elif menu_choice == 4:
        print("Lookup Number")
        name = input("Name: ")  # Prompt for the name
        if name in numbers:  # Check if the name exists in the dictionary
            print("The number is", numbers[name])  # Display the number if found
        else:
            print(name, "was not found")  # Inform the user if the name was not found

    # If any other number (not 1-5), display the menu again
    elif menu_choice != 5:
        print_menu()
