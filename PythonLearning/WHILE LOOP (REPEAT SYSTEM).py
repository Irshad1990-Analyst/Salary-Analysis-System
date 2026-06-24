while True:
    print("\n🏪 Welcome to Shop")
    print("1. Buy Item")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("🛒 Item Purchased")

    elif choice == "2":
        print("👋 Shop Closed")
        break

while True:
    print("\n🧮 SIMPLE CALCULATOR")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "5":
        print("👋 Exiting Calculator...")
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == "1":
        print("Result:", a + b)

    elif choice == "2":
        print("Result:", a - b)

    elif choice == "3":
        print("Result:", a * b)

    elif choice == "4":
        print("Result:", a / b)

    else:
        print("❌ Invalid choice")