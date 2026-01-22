import art

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operators = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
}

def calculator():
    print(art.logo)
    first_num = float(input("What's the first number?: "))
    while True:
        for symbol in operators:
            print(symbol)
        operator = input("Pick an operation: ")
        second_num = float(input("What's the next number?: "))
        result = operators[operator](first_num, second_num)
        print(f"{first_num} {operator} {second_num} =", result)

        continue_calculating = input(f"Type 'y' to continue calculating with {result}, or 'n' to start a new calculation. ")
        if continue_calculating == "y":
            first_num = result
        elif continue_calculating == "n":
            print("\n" * 20)
            calculator()

calculator()