# Define tuples for each person with their first, middle, last names, and age.
# Each tuple represents a person's full name and age.
nancy = ('Nancy', 'Jiano', 'Yang', 18)
daniel = ('Daniel', 'Dingyue', 'Wang', 16)
tobin = ('James', 'Anthony', 'Tobin', 42)

# Initialize an empty list called 'people' to hold the person tuples.
people = []

# Append each person's tuple to the 'people' list.
# This builds a collection of all persons defined.
people.append(nancy)
people.append(daniel)
people.append(tobin)

# Define a function 'firstName' that takes a 'name' tuple as an argument
# and returns the first element of the tuple, which is the first name of the person.
def firstName(name):
    return name[0]

# Define a function 'middleName' that takes a 'name' tuple as an argument
# and returns the second element of the tuple, which is the middle name of the person.
def middleName(name):
    return name[1]

# Define a function 'familyName' that takes a 'name' tuple as an argument
# and returns the third element of the tuple, which is the family or last name of the person.
def familyName(name):
    return name[2]

# Define a function 'age' that takes a 'name' tuple as an argument
# and returns the fourth element of the tuple, which is the age of the person.
def age(name):
    return name[3]

# Print the original list of people to show the unsorted list.
print(people)

# Sort the 'people' list by first name using the 'firstName' function as the key
# and print the sorted list. The 'sorted' function returns a new list.
sorted_by_first_name = sorted(people, key=firstName)
print("Sorted by first name: ", sorted_by_first_name)

# Sort the 'people' list by age using the 'age' function as the key
# and print the sorted list.
sorted_by_age = sorted(people, key=age)
print("Sorted by age: ", sorted_by_age)

# Sort the 'people' list by middle name using the 'middleName' function as the key
# and print the sorted list.
sorted_by_middle_name = sorted(people, key=middleName)
print("Sorted by middle name: ", sorted_by_middle_name)

# Sort the 'people' list by family name using the 'familyName' function as the key
# and print the sorted list.
sorted_by_family_name = sorted(people, key=familyName)
print("Sorted by family name: ", sorted_by_family_name)
