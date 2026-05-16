""" Module to handle all validations """
def validate_item_name(name):
    """ Check if strings are empty, only contains spaces or only numbers
        Args: takes in a name
        Return: True or False
    """
    if not name or name.strip() == "":
        return False, "Error: Item name cannot be empty or just spaces."
    if name.strip().isdigit():
        return False, "Error: Item name cannot be just a number."
    return True, "Valid name."

def get_valid_string(prompt):
    """ helper function to repeatedly ask for a string until valid """
    while True:
        value = input(prompt)
        is_valid, message = validate_item_name(value)
        if is_valid:
            return value.strip()
        print(message)
        
def get_valid_int(prompt):
    """ Helper function to repeatedly ask for an integer until valid """
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print('Error: Number cannot be negative or 0.')
                continue
            return value
        except ValueError:
            print('Error: Please enter a valid number')

""" test_inputs = ["Tomato", "   ", "", "12345", "Tomato 2"]

for user_input in test_inputs:
    is_valid, message = validate_item_name(user_input)
    print(f"Input: '{user_input}' -> Valid: {is_valid} | {message}") """