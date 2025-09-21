import random
options = ["Rock", "Paper", "Scissor"]
computer_choice_number = random.randint(0,2)
user_choice_number = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
computer_choice = options[computer_choice_number]
user_choice = options[int(user_choice_number)]
print("The computer chose: " + computer_choice)
print("You chose: " + user_choice)
if computer_choice == "Rock" and user_choice == "Paper":
    print("You Win")
elif computer_choice == "Rock" and user_choice == "Scissor":
    print("You Lose")
elif computer_choice == "Paper" and user_choice == "Scissor":
    print("You Win")
elif computer_choice == "Paper" and user_choice == "Rock":
    print("You Lose")
elif computer_choice == "Scissor" and user_choice == "Rock":
    print("You Win")
elif computer_choice == "Scissor" and user_choice == "Paper":
    print("You Lose")
elif computer_choice == "Rock" and user_choice == "Rock":
    print("Its a DRAW")
elif computer_choice == "Paper" and user_choice == "Paper":
    print("Its a DRAW")
elif computer_choice == "Scissor" and user_choice == "Scissor":
    print("Its a DRAW")
else:
    print("I think you made a mistake in choosing the numbers. Try again!")
