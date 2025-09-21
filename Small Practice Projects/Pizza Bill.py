print("Welcome to Python Pizza Deliveries!")
size = input("What size do you want your pizza to be? S, M or L? \n")
pepperoni = input("Do you want pepperoni on your pizza? Y or N? \n")
extra_cheese = input("Do you want extra cheese? Y or N?\n")
bill = 0
if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill += 2
    else:
        bill += 0
elif size == "M":
    bill = 20
    if pepperoni == "Y":
        bill += 3
    else:
        bill += 0
else:
    bill = 25
    if pepperoni == "Y":
        bill += 3
    else:
        bill += 0
if extra_cheese == "Y":
    bill +=1
else:
    bill += 0
print(f"Your Pizza is ${bill}")
