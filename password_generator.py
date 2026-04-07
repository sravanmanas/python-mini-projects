# Password Generator using Python

import random
import string

def generate_password():
    
    # Combine all possible characters:
    # - lowercase + uppercase letters
    # - digits (0-9)
    # - special symbols
    symbols = string.ascii_letters

     # Ask user for additional options
    include_digits = input("Include digits? (y/n): ")
    include_symbols = input("Include special characters? (y/n): ")

    # Add digits if user chooses yes
    if include_digits.lower() == "y":
        symbols += string.digits

    # Add special symbols if user chooses yes
    if include_symbols.lower() == "y":
        symbols += string.punctuation

    # Take password length from user
    n = int(input("Enter the length of password: "))

    # Check for valid input
    if n <= 0:
        print("Enter a valid length.\n")
    
    else:
        # Generate password:
        # Loop n times and pick random character each time
        password = "".join(random.choice(symbols) for _ in range(n))

        print("Generated Password:", password)


# Call the function to run the program
generate_password()
