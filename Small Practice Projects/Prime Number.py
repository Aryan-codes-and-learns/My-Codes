number = int(input("Pick a number!"))
true = []
for i in range(1, number+1):
    if number % i == 0:
        true.append("true")
if len(true) == 2:
    print("The number is a prime number!")
else:
    print("The number isn't a prime number.")