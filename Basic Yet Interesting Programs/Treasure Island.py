print("Welcome to the Treasure Island!!!\nYour mission is to find treasure!")
direction = input("Where do you want to go? \nLeft or Right?\n")
if direction == "Left":
    print("You made the right choice!")
    action = input("Oh... you have come across a river.. what do you want to do? \nSwim or Wait??\n")
    if action == "Wait":
        print("Lucky, you made the right choice.")
        door = input("You have multiple doors, which one are you going to choose? \nRed, Blue or Yellow???\n")
        if door == "Yellow":
            print("YOU WON!!!! CONGRATS")
        elif door == "Red":
            print("You got burned by fire and died :(\nGame Over")
        elif door == "Blue":
            print("You got eaten by beasts :( \nGame Over")
        else:
            print("Please choose the doors from the given options. ")
    else:
        print("You got attacked by a trout and died :(\nGame Over")
elif direction == "Right":
    print("You fell into a hole and died :(")
else:
    print("Choose again!")
