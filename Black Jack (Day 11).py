import random

cards_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # The Deck. Ace = 11. J,Q,K = 10
users_cards_values = []
computers_cards_values = []

for i in range(2):  # Used to fill the empty lists above.
    value = random.choice(cards_values)
    users_cards_values.append(value)
    value = random.choice(cards_values)
    computers_cards_values.append(value)

hidden_computer_value = computers_cards_values[1]  # Just a quick substitution to not show the second card.
computers_cards_values[1] = "?"

print(f"The values of your cards are: \n{users_cards_values}")
print(f"The values of the computer's cards are: \n{computers_cards_values}")
computers_cards_values[1] = hidden_computer_value  # After showing the necessary cards. the value is re-substituted

go = True
while go:
    if sum(computers_cards_values) <= 16:  # Did this so that the game isn't too easy for the player.
        value = random.choice(cards_values)
        computers_cards_values.append(value)

    choice = input("Do you want to take another card? Yes or No?\n: ").lower()

    if choice == "yes":
        value = random.choice(cards_values)
        users_cards_values.append(value)
        print(f"Here is your new card set: \n{users_cards_values}")
        print(f"Here is the computer card set: \n{computers_cards_values}")

    elif choice == "no":
        print(f"Here is your card set: \n{users_cards_values}")
        print(f"Here is the computer card set: \n{computers_cards_values}")
        go = False  # Breaks the whole loop once the player decides to stop taking new cards.

    else:
        print("You typed something incorrectly. Answer again")

players_sum = sum(users_cards_values)  # Sums up the player's list
computers_sum = sum(computers_cards_values)  # Sums up the computer's list

if 11 in users_cards_values and players_sum > 21:  # The rule that if the sum is > 21, the ace isn't 11 anymore, but 1.
    users_cards_values.remove(11)
    users_cards_values.append(1)

if 11 in computers_cards_values and computers_sum > 21:
    computers_cards_values.remove(11)
    computers_cards_values.append(1)

print(f"Your total sum is {players_sum}")
print(f"Computer's total sum is {computers_sum}")
if players_sum > 21:
    if computers_sum > 21:
        print("You Both Busted.\nHence, Dealer Wins and You Lose!")
    else:
        print("You Busted\nYou Lose!")
else:
    if computers_sum > 21:
        print("The computer busted. You WIN!!!! Congrats")
    else:
        if players_sum > computers_sum:
            print("You scored higher points. You Win!!! Congrats")
        elif players_sum < computers_sum:
            print("The computer scored higher points. You Lose.")
        elif players_sum == computers_sum:
            print("Since its equal, its a tie!")
        else:  # Just did this because it felt "odd" without an else statement haha. This doesn't affect the code. 
            x = 0
