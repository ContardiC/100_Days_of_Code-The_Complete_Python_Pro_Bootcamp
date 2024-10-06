import art
def add(n1, n2):
    return n1 + n2
# TODO: Write out the other 3 functions - subtract, multiply and divide.

def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.


#print(functions["*"](4,8))

def calculator():
    print(art.logo)
    # TODO: Program asks the user to type the first number.
    n1 = float(input("What's the first number?: "))
    should_accumulate = True
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        n2 = float(input("What's the next number?: "))
        result = operations[operation_symbol](n1, n2)
        print(f"{n1} {operation_symbol} {n2} + {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation: ")
        if choice == 'n':
            should_accumulate = False
            print("\n"*20)
            calculator()
        else:
            n1 = result
calculator()