print("Welcome to the Tip Calculator")
bill = input("What was the total bill?: \n")
Tip = input("How much % Tip Would You Like to Give? 10, 12, or 15? \n")
People = input("How many people to split the bill? \n")
amount = float(bill) * (1+(float(Tip)/100))
each = amount/float(People)
each_rounded = round(each, 2)
print(f"Each Person Should Pay: ${each_rounded}")

