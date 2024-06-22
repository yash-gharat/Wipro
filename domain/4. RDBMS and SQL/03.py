# 3. write a calculator program in python

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        option = (input("Enter the option"));

        if option in ('1',"2","3","4"):
            try:
                num1 = float(input("Enter num1"))
                num2 = float(input("Enter num2"))
            except:
                print("Invalid input")
                continue
            if option == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif option == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif option == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif option == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")

            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    calculator()