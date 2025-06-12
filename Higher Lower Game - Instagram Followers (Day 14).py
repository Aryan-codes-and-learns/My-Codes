import random
data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 180,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 220,
        'description': 'Media personality',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 200,
        'description': 'Actor and wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 210,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 190,
        'description': 'Media personality',
        'country': 'United States'
    },
    {
        'name': 'Beyoncé',
        'follower_count': 170,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Nike',
        'follower_count': 160,
        'description': 'Sportswear brand',
        'country': 'United States'
    },
    {
        'name': 'Justin Bieber',
        'follower_count': 150,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Kendall Jenner',
        'follower_count': 155,
        'description': 'Model',
        'country': 'United States'
    },
    {
        'name': 'National Geographic',
        'follower_count': 140,
        'description': 'Magazine',
        'country': 'United States'
    },
    {
        'name': 'Taylor Swift',
        'follower_count': 135,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Virat Kohli',
        'follower_count': 130,
        'description': 'Cricketer',
        'country': 'India'
    },
    {
        'name': 'Neymar Jr.',
        'follower_count': 125,
        'description': 'Footballer',
        'country': 'Brazil'
    },
    {
        'name': 'Zendaya',
        'follower_count': 120,
        'description': 'Actress and singer',
        'country': 'United States'
    },
    {
        'name': 'Kourtney Kardashian',
        'follower_count': 115,
        'description': 'Media personality',
        'country': 'United States'
    },
    {
        'name': 'LeBron James',
        'follower_count': 110,
        'description': 'Basketball player',
        'country': 'United States'
    },
    {
        'name': 'Shakira',
        'follower_count': 105,
        'description': 'Musician',
        'country': 'Colombia'
    },
    {
        'name': 'Drake',
        'follower_count': 100,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Billie Eilish',
        'follower_count': 95,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Emma Watson',
        'follower_count': 90,
        'description': 'Actress',
        'country': 'United Kingdom'
    }
]

random.shuffle(data)  # Just to add more randomness
a = random.randint(0, 23)  # The index numbers
b = random.randint(0, 23)

same = True
while same:  # This loop is to make sure that a and b are not the same number
    if a == b:
        b = random.randint(1, 23)
    else:
        same = False

print(f"Compare A: {data[a]['name']}, a {data[a]['description']}, from {data[a]['country']}.")
print("VS")
print(f"Compare B: {data[b]['name']}, a {data[b]['description']}, from {data[b]['country']}.")

score = 0  # The initial score of the player.

correct = True  # If the user gets the answer wrong, this becomes false, and the game ends.
while correct:  # This loop is used so that the game can continue if the user gets the answer correct.
    choice = input("Who has more Followers? Type 'A' or 'B': ").lower()
    print("\n\n\n")  # To make it a little visually pleasing in the output box haha.
    old_score = score  # This method is used for the program to know if the user chose the correct answer or not.

    if choice == "a":
        if data[a]['follower_count'] > data[b]['follower_count']:
            print("You are right!")
            score += 1
        elif data[a]['follower_count'] < data[b]['follower_count']:
            print("Sorry, that's wrong.")

    elif choice == "b":
        if data[a]['follower_count'] < data[b]['follower_count']:
            print("You are right!")
            score += 1
        elif data[a]['follower_count'] > data[b]['follower_count']:
            print("Sorry, that's wrong.")

    print(f"{data[a]['name']} has {data[a]['follower_count']} million followers.")
    print(f"{data[b]['name']} has {data[b]['follower_count']} million followers.")

    if data[a]['follower_count'] < data[b]['follower_count']:
        a = b  # This makes sure that the highest following acc is used in the next round.

    if score > old_score:  # Meaning that the answer is correct
        print(f"Current Score: {score}")
        print("Let's Go Again!\n")

        b = random.randint(0, 23)  # Choosing a new value for the second account.
        same = True
        while same:  # This loop is to make sure that a and b are not the same number
            if a == b:
                b = random.randint(1, 23)
            else:
                same = False

        print(f"Compare A: {data[a]['name']}, a {data[a]['description']}, from {data[a]['country']}.")
        print("VS")
        print(f"Compare B: {data[b]['name']}, a {data[b]['description']}, from {data[b]['country']}.")

    elif score == old_score:  # Answer is false (score didn't increase)
        correct = False  # Ends the game.
print(f"Final Score: {score}")
