import random
word_list = ["aryan", "ahan", "anshuman", "ishan", "saritanshu"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False

progress = []
remaining_lives = 6
while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            progress.append(guess)
        elif letter in progress:
            display += letter
        else:
            display += "_"

    print(display)
    if guess not in chosen_word:
        remaining_lives -= 1
        if remaining_lives == 0:
            print("Game Over")
            game_over = True
    print(f"You have {remaining_lives} lives remaining.")

    if "_" not in display:
        print("You Win!")
        game_over = True

