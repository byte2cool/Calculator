print("WELCOME TO THE PYTHON CALCULATOR")
print("Select opertion:")
print(" Type 1 to add ")
print(" Type 2 to subtract ")
print(" Type 3 to multiply ")
print(" Type 4 to divide ")
choice = int(input("Enter choice(1/2/3/4): "))
a = int(input("First number = "))
b = int(input("Second number = "))

def add(a,b):
    s = a + b
    return s

def subtract(a,b):
    difference = a - b
    return difference

def multiply(a,b):
    product = a * b
    return product

def divide(a,b):
    quotient = a / b
    return quotient


if choice == 1:
    print("The answer which you are looking for is ",add(a,b))
elif choice == 2:
    print("The answer which you are looking for is ",subtract(a,b))
elif choice == 3:
    print("The answer which you are looking for is ",multiply(a,b))
elif choice == 4:
    print("The answer which you are looking for is ",divide(a,b))
else:
    print("Invalid choice")

print("THANK YOU FOR CALCULATING WITH US")