def add(a, b):
    result = a + b
    print("Answer: " + str(a) + " + " + str(b) + " = " + str(result) + "\n")
    
def sub(a, b):
    result = a - b
    print("Answer: " + str(a) + " - " + str(b) + " = " + str(result) + "\n")

def mul(a, b):
    result = a * b
    print("Answer: " + str(a) + " * " + str(b) + " = " + str(result) + "\n")

def div(a, b):
    if b != 0:
        result = a / b
        print("Answer: " + str(a) + " / " + str(b) + " = " + str(result) + "\n")
    else:
        print("Error: Cannot divide by zero.\n")
            

print("Welcome to Shubh's Companion!")
while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Addition")
        a = int(input("Enter first operand: "))
        b = int(input("Enter second operand: "))
        add(a, b)
    elif choice == 2:
        print("Subtraction")
        a = int(input("Enter first operand: "))
        b = int(input("Enter second operand: "))
        sub(a, b)
    elif choice == 3:
        print("Multiplication")
        a = int(input("Enter first operand: "))
        b = int(input("Enter second operand: "))
        mul(a, b)
    elif choice == 4:
        print("Division")
        a = int(input("Enter first operand: "))
        b = int(input("Enter second operand: "))
        div(a, b)
    elif choice == 5:
        print("Exited.")
        break
    else: 
        print("Invalid choice. Please select a number from 1 to 5")