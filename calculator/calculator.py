"""a simple calculator application that runs in the command line"""

import sys

# Calculator features:
# addition
# subtraction
# multiplication
# division
# square
# root
# modulo
#

history = []


def add(x, y):
    """function returns x + y"""
    result = x + y
    print(f"{x} + {y} = {result}\n--------------------")

    log_history(x, "+", y, result)


def subtract(x, y):
    """function returns x - y"""
    result = x - y
    print(f"{x} - {y} = {result}\n--------------------")

    log_history(x, "-", y, result)


def multiply(x, y):
    """function returns x multiplied by y"""
    result = x * y
    print(f"{x} * {y} = {result}\n--------------------")

    log_history(x, "*", y, result)


def divide(x, y):
    """function returns x divided by y"""
    result = x / y
    print(f"{x} / {y} = {result}\n--------------------")

    log_history(x, "/", y, result)


def square(x):
    """function returns squared value x"""
    result = x * x
    print(f"{x} squared is {result}\n--------------------")

    log_history(x, "^", x, result)


def root(x):
    """function returns the root of value x"""
    root_constant = 0.5
    result = x ** root_constant
    print(f"The square root of {x} is {result}\n--------------------")

    log_history(x, "**", root_constant, result)


def modulo(x, y):
    """function returns x % y"""
    result = x % y
    print(f"{x} module {y} = {result}\n--------------------")

    log_history(x, "%", y, result)


def log_history(x, operator, y, result):
    """function handling the logging of calculation history"""
    history.append(f"{x} {operator} {y} = {result}")


def show_history():
    """function handling the displaying of calculation history"""
    if not history:
        print("No history to show!\n--------------------")
    else:
        print("Previous calculations (oldest first): ")
        for item in history:
            print(item)
        print("--------------------")


def main():
    """the main application function"""

    while True:
        choice = input(
            "\nWhat would you like to do?\n"
            "'add' to perform addition,\n"
            "'sub' to perform subtraction,\n"
            "'mult' to perform multiplication,\n"
            "'div' to perform division,\n"
            "'square' to square a number,\n"
            "'root' to find the square root of a number,\n"
            "'mod' to perform a modulo operation on two numbers,\n"
            "'history' to see operation history,\n"
            "'exit' to close the app\n"
            ": "
        )
        print("\n--------------------")
        match choice.strip().lower():
            case "add":
                while True:
                    try:
                        x = int(input("Enter first number to be added: "))
                        break
                    except ValueError:
                        print("Not a number!")
                while True:
                    try:
                        y = int(input("Enter second number: "))
                        break
                    except ValueError:
                        print("Not a number!")
                add(x, y)
            case "sub":
                while True:
                    try:
                        x = int(input("Enter the number to subtract from: "))
                        break
                    except ValueError:
                        print("Not a number!")
                while True:
                    try:
                        y = int(input("How much do you want to subtract by: "))
                        break
                    except ValueError:
                        print("Not a number!")
                subtract(x, y)
            case "mult":
                while True:
                    try:
                        x = int(
                            input("Enter the first number to be multiplied: "))
                        break
                    except ValueError:
                        print("Not a number!")
                while True:
                    try:
                        y = int(
                            input("Enter the second number for multiplication: "))
                        break
                    except ValueError:
                        print("Not a number!")
                multiply(x, y)
            case "div":
                while True:
                    try:
                        x = int(input("Enter the dividend: "))
                        break
                    except ValueError:
                        print("Not a number!")
                while True:
                    try:
                        y = int(input("Enter the divisor: "))
                        break
                    except ValueError:
                        print("Not a number!")
                divide(x, y)
            case "square":
                while True:
                    try:
                        x = int(input("What number do you want to square: "))
                        break
                    except ValueError:
                        print("Not a number!")
                square(x)
            case "root":
                while True:
                    try:
                        x = int(
                            input("What number do you want to find the square root for: "))
                        break
                    except ValueError:
                        print("Not a number!")
                root(x)
            case "mod":
                while True:
                    try:
                        x = int(
                            input("Enter the first number for the modulo evaluation: "))
                        break
                    except ValueError:
                        print("Not a number!")
                while True:
                    try:
                        y = int(
                            input("Enter the second number for the modulo evaluation: "))
                        break
                    except ValueError:
                        print("Not a number!")
                modulo(x, y)
            case "history":
                show_history()
            case "exit":
                sys.exit()
            case _:
                print("\nInvalid option, try again.")


if __name__ == "__main__":
    main()
