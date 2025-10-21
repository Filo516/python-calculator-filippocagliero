def calculate(num1, num2, operation):
    """
    This function performs basic math operations on two numbers.
    It takes three parameters: two numbers and an operation type.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:  # Prevent division by zero
            return num1 / num2
        else:
            return "Error: Cannot divide by zero!"
    else:
        return "Error: Invalid operation!"

def main():
    """
    Main function that handles user interaction and runs the calculator.
    """
    print("=== Simple Calculator ===")
    print("Welcome to the calculator program!")
    print()
    
    # Ask user for two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Please enter valid numbers!")
        return
    
    # Ask user for operation choice
    print("\nWhat operation would you like to perform?")
    print("1. Add")
    print("2. Subtract") 
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter your choice (1-4): ")
    
    # Convert choice to operation name
    if choice == "1":
        operation = "add"
    elif choice == "2":
        operation = "subtract"
    elif choice == "3":
        operation = "multiply"
    elif choice == "4":
        operation = "divide"
    else:
        print("Invalid choice! Please run the program again.")
        return
    
    # Perform calculation using our function
    result = calculate(num1, num2, operation)
    
    # Print the result clearly
    print(f"\nResult: {num1} {operation} {num2} = {result}")
    print("Thank you for using the calculator!")

# Run the program
if __name__ == "__main__":
    main()

