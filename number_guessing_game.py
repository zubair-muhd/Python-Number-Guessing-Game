import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You got it in {attempts} attempts!")
                return
            print(f"Attempts remaining: {max_attempts - attempts}")
        except ValueError:
            print("Please enter a valid number.")
            continue

    print(f"Game Over! The number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()