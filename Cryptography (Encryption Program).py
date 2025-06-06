# Start with having two lists where one is the list with real values and the other one is randomized.

alphabet_list =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
  'u', 'v', 'w', 'x', 'y', 'z', ':', '!', '?', '.',
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
  'U', 'V', 'W', 'X', 'Y', 'Z',
  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
  '%', '(', ')', '@', ',', ' ', "'"]

random_letters = ['%', 'X', 't', 'x', '4', 'b', 'q', '!', 's', '1', 'v', 'G', '5', 'Z', 'a', 'H', 'Y', '.', 'U', '6',
 ' ', 'M', '(', 'N', '@', '0', 'P', 'u', 'f', 'e', "'", 'T', 'o', '9', 'J', 'O', 'm', 'V', 'l', '3',
 'r', 'w', 'R', 'I', 'j', 'W', 'S', ':', 'z', 'g', 'k', 'L', 'n', 'y', '?', 'C', 'D', 'B', 'h', 'c',
 '7', '2', 'E', ',', 'Q', 'K', ')', 'p', 'F', 'i', '8', 'd', 'A']

# Since the positions of items in the list are completely different in the two lists.
# The index numbers varies for each letter, number, symbol. If someone types "a", it will come out as "%".
# Empty lists so that I can append and then join to create the proper sentence.
final_decoded_message_list = []
final_encrypted_message_list = []

# A welcome and a choice whether to encode or decode.
print("Welcome to the Cryptography Station!")
choice = input("What do you want to do? \nEncode or Decode?\n: ").lower()
# The if statements are used here so that the user can do BOTH in 1 program. I wont need to write two different codes.
if choice == "encode":
    message = input("What is your message?: ")
    message_list = list(message)
    # Creates the input into a list.
    length_of_message = len(message_list)
    # This loop goes through every variable of the user string + uses the index for each one to encrypt the letters.
    for i in range(length_of_message):
        letter = message_list[i]
        letter_number = alphabet_list.index(letter)
        # Finds out the index number of the inputted string (out of the first list)
        encrypted_letter = random_letters[letter_number]
        # Encrypts it by inserting that index number into the other list.
        final_encrypted_message_list.append(encrypted_letter)

    final_encrypted_message = "".join(final_encrypted_message_list)
    print(final_encrypted_message)

elif choice == "decode":
    encrypted_message = input("What is your secret message?: ")
    encrypted_message_list = list(encrypted_message)
    length_of_message = len(encrypted_message_list)
    for i in range(length_of_message):
        letter = encrypted_message_list[i]
        letter_number = random_letters.index(letter)
        # Finds out the index number of the inputted string (out of the second list)
        decoded_letter = alphabet_list[letter_number]
        # Decrypts it by inserting that index number into the other list
        final_decoded_message_list.append(decoded_letter)

    final_decoded_message = "".join(final_decoded_message_list)
    print(final_decoded_message)
else:
    print("You made a typo! Choose Again")
