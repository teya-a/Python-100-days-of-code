import subprocess
from art import logo
from functions import operations


def calculator():
    print(logo)

    num1 = float(input("What's the first number?\n: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation\n: ")
        num2 = float(input("What's the next number?\n: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            subprocess.run("clear")
            print(logo)
            num1 = answer
        else:
            should_continue = False
            subprocess.run("clear")
            calculator()


calculator()
