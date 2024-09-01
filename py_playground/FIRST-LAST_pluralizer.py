def pluralize(quantity, singular, plural):
    # Check if the quantity is 1; if so, use the singular form of the noun.
    if quantity == 1:
        return f"{quantity} {singular}"
    else:
        # If the quantity is not 1, use the plural form of the noun.
        return f"{quantity} {plural}"

# Test the function with the provided examples
print(pluralize(1, "cat", "cats")) 
print(pluralize(3, "item", "items")) 
print(pluralize(7, "octopus", "octopi")) 