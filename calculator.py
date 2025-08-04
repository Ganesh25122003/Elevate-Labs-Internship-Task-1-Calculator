def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def main():
    while True:
        print("\n=== Simple Calculator ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose an operation (1-5): ")
        ch=choice
        if ch == '5':
            print("Exiting calculator!")
            break
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if ch == '1':
            print("Result:", add(num1, num2))
        elif ch == '2':
            print("Result:", subtract(num1, num2))
        elif ch == '3':
            print("Result:", multiply(num1, num2))
        elif ch== '4':
            print("Result:", divide(num1, num2))
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()