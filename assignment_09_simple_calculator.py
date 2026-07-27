
def addition(a, b):
    """Perform addition."""
    return a + b


def subtraction(a, b):
    """Perform subtraction."""
    return a - b


def multiplication(a, b):
    """Perform multiplication."""
    return a * b


def division(a, b):
    """Perform division with zero check."""
    if b == 0:
        return "Error: Cannot divide by zero."
    return round(a / b, 2)


def modulus(a, b):
    """Perform modulus (remainder)."""
    if b == 0:
        return "Error: Cannot divide by zero."
    return a % b


def exponentiation(a, b):
    """Perform exponentiation."""
    return a ** b


def display_menu():
    """Display the calculator menu."""
    print("\n" + "=" * 28)
    print("     SIMPLE CALCULATOR")
    print("=" * 28)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")
    print("=" * 28)



if __name__ == "__main__":
    print("=== CALCULATOR STARTED ===\n")
    
    while True:
        display_menu()
        choice = input("Select an operation (1-7): ").strip()
        
        if choice == "7":
            print("Goodbye!")
            break
        
        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Error: Invalid choice. Please select 1-7.")
            continue

        
        try:
            first = float(input("Enter first number : "))
            second = float(input("Enter second number: "))
        except ValueError:
            print("Error: Please enter valid numbers.")
            continue

        
        if choice == "1":
            result = addition(first, second)
            print(f"Result: {first} + {second} = {result}")
        elif choice == "2":
            result = subtraction(first, second)
            print(f"Result: {first} - {second} = {result}")
        elif choice == "3":
            result = multiplication(first, second)
            print(f"Result: {first} * {second} = {result}")
        elif choice == "4":
            result = division(first, second)
            print(f"Result: {first} / {second} = {result}")
        elif choice == "5":
            result = modulus(first, second)
            print(f"Result: {first} % {second} = {result}")
        elif choice == "6":
            result = exponentiation(first, second)
            print(f"Result: {first} ** {second} = {result}")