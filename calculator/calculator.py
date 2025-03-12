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
    print(f"{x} + {y} = {result}")

    history.append(f"{x}+{y}= {result}")


def subtract(x, y):
    """function returns x - y"""


def multiply(x, y):
    """function returns x multiplied by y"""


def divide(x, y):
    """function returns x divided by y"""


def square(x):
    """function returns squared value x"""


def root(x):
    """function returns the root of value x"""


def modulo(x, y):
    """function returns x % y"""


def main():
    """the main application function"""

    while True:
        choice = input(
            "\nWhat would you like to do?\n"
            "'add' to perform addition,\n"
            # "'sub' to perform subtraction,\n"
            # "'multi' to perform multiplication,\n"
            # "'div' to perform division,\n"
            # "'square' to square a number,\n"
            # "'root' to find the root of a number,\n"
            # "'mod' to perform a modulo operation on two numbers,\n"
            "'history' to see operation history,\n"
            "'exit' to close the app\n"
            ": "
        )
        match choice.strip().lower():

            case "add":
                while True:
                    try:
                        x = int(input("\nEnter first number to be added: "))
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

            case "history":
                print(f"\nPrevious operations: {history}")
            case "exit":
                sys.exit()
            case _:
                print("\nInvalid option, try again.\n")


if __name__ == "__main__":
    main()
