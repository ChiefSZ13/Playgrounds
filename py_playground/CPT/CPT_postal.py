import requests  # Import the requests library to make HTTP requests

# Function to get the location details by postal code using the Zippopotam API
def get_location_by_postal_code(postal_code):
    response = requests.get(f"http://api.zippopotam.us/us/{postal_code}")
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Return a dictionary with the city and state
        return {
            "city": data['places'][0]['place name'],
            "state": data['places'][0]['state abbreviation']
        }
    else:
        # If the request was not successful, return None
        return None

# Dictionary to store searched postal codes and their corresponding locations
searched_postal_codes = {}

# Infinite loop to continuously ask for user input
while True:
    postal_code = input("Enter a US postal code (or 'history' to view search history, 'exit' to quit): ")
    # Exit the loop if user inputs 'exit'
    if postal_code.lower() == 'exit':
        break
    # Display search history if user inputs 'history'
    elif postal_code.lower() == 'history':
        # Check if there is any search history
        if searched_postal_codes:
            print("Search History:")
            # Iterate through the search history
            for code, location in searched_postal_codes.items():
                print(f"Postal code: {code}, Address: {location['city']}, {location['state']}")
        else:
            # If no search history is available
            print("No search history available.")
    # Handle regular postal code input
    else:
        # Check if the postal code has already been searched
        if postal_code in searched_postal_codes:
            # Retrieve location from search history
            location = searched_postal_codes[postal_code]
        else:
            # If the postal code is new, fetch location details from the API
            location = get_location_by_postal_code(postal_code)
            # If a valid location is found, save it to the search history
            if location:
                searched_postal_codes[postal_code] = location
        
        # If a valid location is found, display the details
        if location:
            print(f"The postal code {postal_code} corresponds to {location['city']}, {location['state']}.")
        else:
            # If the postal code is invalid, notify the user
            print("Invalid postal code. Please try again.")

# Output all searched postal codes at the end of the program
print("Searched postal codes:", searched_postal_codes)
