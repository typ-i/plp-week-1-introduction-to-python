def calc():
    # Getting user input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    # Performing calculations based on input operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"

    # Returning formatted result
    return f"{num1} {operation} {num2} = {result}"

# Running the calculator
if __name__ == "__main__":
    print("Python Calculator")
    print(calc())
