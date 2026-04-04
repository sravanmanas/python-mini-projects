# Password Generator using Python

import random
import string

def generate_password():
    
    # Combine all possible characters:
    # - lowercase + uppercase letters
    # - digits (0-9)
    # - special symbols
    symbols = string.ascii_letters + string.digits + string.punctuation

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
