def actions():
    print("1 or + -> Addition")
    print("2 or - -> Subtraction")
    print("3 or * -> Multiplication")
    print("4 or / -> Division")
    print("e -> exit")
    while True:
        action = input("\nChoose an action (+, -, *, /) or 'e' to exit: ")
    
        if action == "e":
            print("Exiting...")
            break 
        
        # Validate action BEFORE asking for numbers
        if action not in ["1", "+", "2", "-", "3", "*", "4", "/"]:
            print("Invalid action! Try again.")
            continue # Restarts the loop immediately

        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        except ValueError:
            print("Error: Please enter numbers only.")
            continue # Skips the math and restarts the loop

        # Perform the math
        if action == "1" or action == "+":
            add(x,y)
        elif action == "2" or action == "-":
            sub(x,y)
        elif action == "3" or action == "*":
            multi(x,y)
        elif action == "4" or action == "/":
            if y == 0:
                print("Error: Cannot divide by zero!")
            else:
                division(x,y)

def add(x:float,y:float):
    result = x + y
    print(f"Addition result: {result}")

def sub(x:float,y:float):
    result = x - y
    print(f"Subtraction result: {result}")

def multi(x:float,y:float):
    result = x * y
    print(f"Multiplication result: {result}")

def division(x:float,y:float):
    result = x / y
    print(f"Division result: {result}")

actions()