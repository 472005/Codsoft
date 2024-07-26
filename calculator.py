def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        print("Select the operation you need to perform:")
        print(" a. Addition (+)")
        print(" b. Subtraction (-)")
        print(" c. Multiplication (*)")
        print(" d. Division (/)")
        operation = input("Enter the operation (a/b/c/d): ")
        
        if operation in ('a', '+'):
            result = num1 + num2
            operator = '+'
        elif operation in ('b', '-'):
            result = num1 - num2
            operator = '-'
        elif operation in ('c', '*'):
            result = num1 * num2
            operator = '*'
        elif operation in ('d', '/'):
            if num2 != 0:
                result = num1 / num2
                operator = '/'
            else:
                result = "undefined (division by zero)"
                operator = '/'
        else:
            result = "invalid operation"
            operator = ''
        
        print(f"The result of {num1} {operator} {num2} is: {result}")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

# Invoking the function
calculator()
