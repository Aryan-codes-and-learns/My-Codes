flavors = [{'Water': 50,    # The Dictionary for flavors.
            'Coffee': 18,
            'Milk': 0,
            'Price': 1.5
            },
           {'Water': 200,
            'Coffee': 24,
            'Milk': 150,
            'Price': 2.5
            },
           {'Water': 250,
            'Coffee': 24,
            'Milk': 100,
            'Price': 3
            }]

resources = {'Water': 300,   # The dictionary for resources
             'Coffee': 100,
             'Milk': 200,
             'Money': 0}

machine_on = True  # A condition to keep the loop going (or to end it)
while machine_on:  # A while loop is used so that the machine can be used until it is manually turned off.
    user_wants = input("What would you like? (espresso/latte/cappuccino/report): ").lower()
    index_number = 3  # This index number will be used in the list 'flavors' to identify which coffee is needed.

    if user_wants == "espresso":  # Assigning index values to the flavors
        index_number = 0
        print(f"Price for {user_wants}: {flavors[index_number]['Price']} ")
    elif user_wants == "latte":
        index_number = 1
        print(f"Price for {user_wants}: {flavors[index_number]['Price']} ")
    elif user_wants == "cappuccino":
        index_number = 2
        print(f"Price for {user_wants}: {flavors[index_number]['Price']} ")
    elif user_wants == "report":  # Gives a report of the remaining resources.
        print(f"Water: {resources['Water']}ml\nMilk: {resources['Milk']}ml\nCoffee: {resources['Coffee']}g\nMoney: ${resources['Money']}")
    elif user_wants == "off":  # To turn the coffee machine off.
        machine_on = False
        print("Machine Turned Off.")

    if index_number < 3:  # Stops the program from asking to insert coins if i want a report or to turn it off.

        price = flavors[index_number]['Price']

        sufficient = True

        if resources['Water'] < flavors[index_number]['Water']:  # Checks if there's enough water.
            print("Sorry, there is not enough water.")
            sufficient = False
        if resources['Milk'] < flavors[index_number]['Milk']: # Checks if there's enough milk.
            print("Sorry, there is not enough milk.")
            sufficient = False
        if resources['Coffee'] < flavors[index_number]['Coffee']: # Checks if there's enough coffee.
            print("Sorry, there is not enough coffee powder.")
            sufficient = False

        if sufficient:  # Continues the process ONLY if every material is sufficient.

            print("Please Insert Coins")
            quarters = int(input("How Many Quarters?: "))
            dimes = int(input("How Many Dimes?: "))
            nickels = int(input("How Many Nickels?: "))
            pennies = int(input("How Many Pennies?: "))

            paid_money = (quarters*0.25) + (dimes*0.1) + (nickels*0.05) + (pennies*0.01)

            if paid_money < price:
                print("Sorry that's not enough money. Money Refunded.")
            elif paid_money >= price:
                pre_change = paid_money - price  # pre_change is just another variable for change but NOT rounded.
                change = round(pre_change, 2)
                if paid_money > price:  # So that it will not print the change ($0) if the money is EXACT.
                    print(f"Here is ${change} in change.")

                a = resources['Money']  # 'a' is just the temporary variable with the old value of money to sum them.
                a += price
                resources['Money'] = a  # Updates the data in the dictionary to the new value.

                w = resources['Water']  # 'w' is just the temporary variable with the old value of quantity of water.
                w -= flavors[index_number]['Water']
                resources['Water'] = w  # Updates the data in the dictionary to the new value.

                m = resources['Milk']  # 'm' is just the temporary variable with the old value of quantity of milk.
                m -= flavors[index_number]['Milk']
                resources['Milk'] = m  # Updates the data in the dictionary to the new value.

                c = resources['Coffee']  # 'c' is just the temporary variable with the old value of quantity of coffee.
                c -= flavors[index_number]['Coffee']
                resources['Coffee'] = c  # Updates the data in the dictionary to the new value.

                print(f"Here is your {user_wants} ☕ ENJOY!")
