# ------ ADVANCED CALCULATOR ------
import math

#MENU 

def show_menu():
    print("\n============= Advanced Calculator ================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Percentage")
    print("8. Exit")

# Input Function

def take_two_numbers():
    while True:
        
        try:
            first_number = float(input("Enter first number = "))
            second_number = float(input("Enter second number = "))

            return first_number, second_number
        
        except ValueError:
            print("Invalid input! please enter numbers only.")

def take_one_number():

    while True:
        try:
            number = float(input("Enter number = ")) 
            return number

        except ValueError:
            print("Invalid input! please enter a valid number.")

    
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

def power(a, b):
    return math.pow(a,b)

def square_root(number):
    
    if number < 0:
        return "Error : Square root of negative numbers is not possible."
    return math.sqrt(number)

def percentage():
       
        part, whole = take_two_numbers()

        if whole == 0:
            return "Error: Whole value cannot be zero."
           
        return (part / whole) * 100

# operations

operations = {
    "1": add,
    "2": subtract,
    "3": multiply,
    "4": divide,
    "5": power
}

while True:
    show_menu()

    choice = input("Enter your choice!  ")

    if choice in operations:
        a, b = take_two_numbers()
        result = operations[choice](a, b)
        print(f"\nResult = {result}\n")
 
    # Square Root 
    elif choice == "6": 
        number = take_one_number() 
        result = square_root(number) 
        print(f"\nResult = {result}\n")
    
    # Percentage
    elif choice == "7":
        result = percentage()
        print(f"\nPercentage = {result}%\n")

    #Exiting
    elif choice == "8":
        print("Program Exiting...!")
        break
    
    #Invalid Choice
    else:
        print("Invalid choice! please select from menu.")