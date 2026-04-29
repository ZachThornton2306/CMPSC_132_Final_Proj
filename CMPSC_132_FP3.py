#CMPSC 132 Final Project
#Choice Number 3: Number Guessing Game

import random


def choose_difficulty():
    # Ask the player to choose difficulty level
    # Returns a dict containing game settings

    difficulties = {
        "1": {"name": "Easy", "low": 1, "high": 50, "max_attempts": None},
        "2": {"name": "Medium", "low": 1, "high": 100, "max_attempts": 10},
        "3": {"name": "Hard", "low": 1, "high": 200, "max_attempts": 8},
    }

    print("\nChoose a difficulty:")
    print("1. Easy - Guess 1 to 50, unlimited attempts")
    print("2. Medium - Guess 1 to 100, 10 attempts")
    print("3. Hard - Guess 1 to 200, 8 attempts")

    while True:
        choice = input("Enter 1, 2, or 3: ").strip()

        if choice in difficulties:
            return difficulties[choice]
        
        print("Inalid choice. Please enter 1, 2, or 3.")


def get_valid_guess(low, high, previous_guesses):
    # Gets a valid integer guess from the player
    # Makes sure the input is a number and inside the allowed range

    while True:
        guess_input = input(f"Enter your guess ({low}-{high}): ").strip()

        try:
            guess = int(guess_input)

            if guess < low or guess > high:
                print(f"Your guess must be between {low} and {high}.")
            elif guess in previous_guesses:
                print("You already guessed that number. Try a different one.")
            else:
                return guess
            
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def give_feedback(guess, secret_number):
    # Gives the player feedback based on their guess

    if guess > secret_number:
        print("Too high! Try guessing a lower number.")
    elif guess < secret_number:
        print("Too low! Try guessing a higher number.")
    else:
        print("Correct!")


def play_game():
    # Runs one full round of the number guessing game

    settings = choose_difficulty()
    low = settings["low"]
    high = settings["high"]
    max_attempts = settings["max_attempts"]

    secret_number = random.randint(low, high)
    attempts = 0
    previous_guesses = []

    print(f"\nYou selected {settings['name']} mode.")
    print(f"I am thinking of a number betweeen {low} and {high}.")

    if max_attempts is None:
        print("You have unlimited attempts.")
    else:
        print(f"You have {max_attempts} attempts.")

    while True:
        if max_attempts is not None:
            remaining = max_attempts - attempts
            print(f"\nAttempts remaining: {remaining}")

        guess = get_valid_guess(low, high, previous_guesses)
        previous_guesses.append(guess)
        attempts += 1

        give_feedback(guess, secret_number)

        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempt(s).")
            print(f"Your guesses were: {previous_guesses}")
            break

        if max_attempts is not None and attempts >= max_attempts:
            print("\nGame over! You ran out of attempts.")
            print(f"The correct number was {secret_number}.")
            print(f"Your guesses were: {previous_guesses}")
            break

def ask_to_play_again():
    # Asks the player if they want to play another round
    # Returns True for yes and False for no

    while True:
        answer = input("\nWould you like to play again? (yes/no): ").strip().lower()

        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            print("Please enter yes or no.")


def main():
    # Main function that starts the program

    print("Welcome to the Number Guessing Game!")

    while True:
        play_game()

        if not ask_to_play_again():
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
