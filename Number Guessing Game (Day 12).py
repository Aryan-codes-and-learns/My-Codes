import random

print("Welcome to the Number Guessing Game\nI am thinking of a number between 1 and 100.")
difficulty = input("Choose a Difficulty. Type 'Easy' or 'Hard'\n: ").lower()
tries = 0  # This is the variable for the amount of tries that the player has.

if difficulty == "easy":
    tries = 10
    print(f"You have {tries} tries to guess the correct number!")
elif difficulty == "hard":
    tries = 5
    print(f"You have {tries} tries to guess the correct number!")
else:
    print("You made some typing error.")

number = random.randint(1, 100)
while tries != 0:
    guess = int(input("Make your guess. Choose a number.\n: "))

    if guess > number:
        print("Too High")
        tries -= 1
        print(f"You have {tries} tries left.")
    elif guess < number:
        print("Too Low")
        tries -= 1
        print(f"You have {tries} tries left.")
    elif guess == number:
        print("Congratss!! You guessed it right")
        tries = 0  # Just a cheap and simple way of ending the loop.

if guess != number:
    print(f"You ran out of tries. Better luck next time.\nThe number was {number}")
