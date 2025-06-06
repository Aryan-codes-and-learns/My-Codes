print("Welcome to the secret auction area")

#Take the input from the person that enters their values first.

first_name = input("What is your name?: ")
first_bid_string = input("What is your bid?: ")
first_bid = int(first_bid_string)

# A list will keep track of all the names and the bids.

names = [first_name]
bids = [first_bid]

# This is just a self-explanatory while loop.

enough_bidders = False
while not enough_bidders:
    more_bidders = input("Are there more bidders? Answer only in Yes or No").lower()
    if more_bidders == "yes":
        # The use of multiple \n is made to "clear the screen" before the next person enters their name and value.
        name = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWhat is your name?: ")
        names.append(name)
        bid_string = input("What is your bid?: ")
        bid = int(bid_string)
        bids.append(bid)
    elif more_bidders == "no":
        enough_bidders = True
    else:
        # Just in case someone says something other than "yes" or "no"
        print("Huh? Type it again!")
# since the bids are added along side the name, then they would have the same index number.
# this index number can be used to easily connect the two lists.
highest_bid = max(bids)
index_number_of_the_highest_bid = bids.index(highest_bid)
person_with_the_highest_bid = names[index_number_of_the_highest_bid]

print(f"\n\n\n\nThe person that won this auction is.... {person_with_the_highest_bid} with a bid of ${highest_bid}!!! ")
print(f"Congratulations {person_with_the_highest_bid}")