import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = ""

for password_letters in range(1, (nr_letters + 1)):
    random_letters_positions = random.randint(1, len(letters)-1)
    password = password + letters[random_letters_positions]

for password_symbols in range(1, (nr_symbols + 1)):
    random_symbols_positions = random.randint(1, len(symbols)-1)
    password = password + symbols[random_symbols_positions]

for password_numbers in range(1, (nr_numbers + 1)):
    random_numbers_positions = random.randint(1, len(numbers)-1)
    password = password + numbers[random_numbers_positions]

password = list(password)
random.shuffle(password)
shuffled_password = "".join(password)
print(shuffled_password)