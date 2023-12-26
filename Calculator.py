def add(a, b):
    result = a + b
    print(str(a) + " + " + str(b) + " = " + str(result))
    
def sub(a, b):
    result = a - b
    print(str(a) + " - " + str(b) + " = " + str(result))

def mul(a, b):
    result = a * b
    print(str(a) + " * " + str(b) + " = " + str(result))

def div(a, b):
    result = a / b
    print(str(a) + " / " + str(b) + " = " + str(result))

print("Welcome to Shubh's Companion!")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

choice = input("Enter your choice: ")

if choice == "1":
    print("Addition")
    a = int(input("Enter first operand: "))
    b = int(input("Enter second operand: "))
    add(a, b)
elif choice == "2":
    print("Subtraction")
    a = int(input("Enter first operand: "))
    b = int(input("Enter second operand: "))
    sub(a, b)
    