def add(a, b):
    """This is a function to add two numbers"""
    return a + b


def subtract(a, b):
    """This is a function to subtract two numbers"""
    return a - b


def multiply(a, b):
    """This is a function to multiply two numbers"""
    return a * b


def divide(a, b):
    """This is a function to divide two numbers"""
    return a / b


def calculate(first_number, second_number):
    """This is a function that combines the previous 4 functions (using if and else) and calculates the answer.
    I created this separate function to combine all of them to reduce the total lines of code. I can simply use this
    function to perform whatever calculations."""
    if choice == "+":
        answer = add(first_number, second_number)
        return answer
    elif choice == "-":
        answer = subtract(first_number, second_number)
        return answer
    elif choice == "*":
        answer = multiply(first_number, second_number)
        return answer
    elif choice == "/":
        answer = divide(first_number, second_number)
        return answer
    else:
        print("type correctly bruv")
stop = False
while not stop:
    first_number = int(input("Enter your first number: "))
    choice = input("Do you want to Add, Subtract, Multiply, or Divide? \n+\n-\n*\n/\n: ")
    second_number = int(input("Enter your second number: "))
    answer = calculate(first_number, second_number)
    print(f"{first_number} {choice} {second_number} = {answer}")
    # Another while loop is needed to keep calculating if the user wishes to.
    go_on = True
    while go_on:
        lets_go = input("Press 'y' to cotninue, 'n' to start over and 'x' to STOP\n: ").lower()
        if lets_go == "y":
            first_number = answer  # the previous calculated answer is treated as the "first number"
            choice = input("Do you want to Add, Subtract, Multiply, or Divide? \n+\n-\n*\n/\n: ")
            second_number = int(input("Enter your second number: "))
            answer = calculate(first_number, second_number)
            print(f"{first_number} {choice} {second_number} = {answer}")
        elif lets_go == "n":  # to start a new calculation
            go_on = False
        elif lets_go == "x":  # to stop both loops and turn the calculator off
            stop = True
            go_on = False
            print("\n\n\n\n\n\nFinished Calculating!")  # Just to make it visually pleasing!
            print(f"Your final answer is = {answer}")
        else:
            print("You typed something else. type correctly bruv.")  # Just in case somebody inputs something else.
