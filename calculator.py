import math

# ---------- Utility Functions ----------

def get_number(prompt):
    """Ensures only valid numbers are entered"""
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("❌ Characters are not allowed. Please enter a valid number.")

# ---------- Operations ----------

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "❌ Cannot divide by zero"
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b

def square_root(a):
    if a < 0:
        return "❌ Cannot find square root of negative number"
    return math.sqrt(a)

# ---------- Main Calculator ----------

def calculator():
    print("=== 🔥 Advanced CLI Calculator ===")

    while True:
        print("\nChoose operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Power (x^y)")
        print("6. Square Root (√x)")
        print("7. Modulus (%)")
        print("8. Exit")

        choice = input("Enter choice (1-8): ")

        if choice == '8':
            print("👋 Exiting... Thank you!")
            break

        if choice not in ['1','2','3','4','5','6','7']:
            print("❌ Invalid choice. Please select 1–8.")
            continue

        # Square root case
        if choice == '6':
            num = get_number("Enter number: ")
            result = square_root(num)

        else:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)
            elif choice == '5':
                result = power(num1, num2)
            elif choice == '7':
                result = modulus(num1, num2)

        print("✅ Result:", result)


if __name__ == "__main__":
    calculator()