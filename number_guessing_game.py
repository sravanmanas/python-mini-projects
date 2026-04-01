import random

def game():
    print("===== Number Guessing Game =====")
    print("Guess a number between 1 and 100\n")

    # Generate a random number between 1 and 100
    number = random.randint(1, 100)

    # Track number of attempts
    attempts = 0

    # Run the game loop until correct guess
    while True:
        try:
            # Take user input and convert to integer
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check if guess is too low
            if guess < number:
                print("Too low! Try higher.\n")

            # Check if guess is too high
            elif guess > number:
                print("Too high! Try lower.\n")

            # Correct guess
            else:
                print(f"🎉 Correct! You guessed it in {attempts} attempts.")
                break

        # Handle invalid input
        except ValueError:
            print("Please enter a valid number!\n")

# Start the game
game()
