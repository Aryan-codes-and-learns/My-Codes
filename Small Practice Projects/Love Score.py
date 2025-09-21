name1 = input("What is your name?").lower()
name2 = input("What is your partners name?").lower()
name1 = "Lmao"
name2 = "lmfao"
combined_name = name1 + name2
combined_name_list = list(combined_name)

def calculate_love_score():
    true = 0
    love = 0
    for letter in combined_name_list:
        if letter == "t":
            true += 1
        elif letter == "r":
            true += 1
        elif letter == "u":
            true += 1
        elif letter == "e":
            true += 1
        else:
            true += 0

        if letter == "l":
            love += 1
        elif letter == "o":
            love += 1
        elif letter == "v":
            love += 1
        elif letter == "e":
            love += 1
        else:
            love += 0
    love_score = str(true) + str(love) + "%"
    print(love_score)

calculate_love_score()