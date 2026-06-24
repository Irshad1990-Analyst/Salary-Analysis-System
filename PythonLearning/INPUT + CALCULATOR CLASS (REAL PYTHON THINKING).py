a = input('Enter First number: ')
b = input('Enter Second number: ')
print(a+b)

a = int(input('Enter First number: '))
b = int(input('Enter Second number: '))
print(a+b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Choose operation:")
print("1 for +")
print("2 for -")
print("3 for *")
print("4 for /")

choice = input("Enter choice: ")

if choice == "1":
    print("Result:", a + b)

elif choice == "2":
    print("Result:", a - b)

elif choice == "3":
    print("Result:", a * b)

elif choice == "4":
    print("Result:", a / b)

else:
    print("Invalid choice")