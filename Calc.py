print("Epic calculator")

running = True

while running:
    pickingNumbers = True
        
    while pickingNumbers:
        inputNum1 = True
        while inputNum1:
            strnum1 = input("Input a number: ")

            if strnum1.isnumeric() == False:
                print("Invalid input")
            else:
                inputNum1 = False
                num1 = int(strnum1)
        
        
        inputNum2 = True
        while inputNum2:
            strnum2 = input("Input another number: ")
            
            
            if strnum2.isnumeric() == False:
                print("Invalid input")
            else:
                inputNum2 = False
                num2 = int(strnum2)
                pickingNumbers = False
                
pickingOperator = True

while pickingOperator:
    choice = input("Pick an operator +, -, *, /, %")

    if choice == "+":
        print(num1 + num2)
        pickingOperator = False
    elif choice == "-":
        print(num1 - num2)
        pickingOperator = False
    elif choice == "*":
        print(num1 * num2)
        pickingOperator = False
    elif choice == "/":
        print(num1 / num2)
        pickingOperator = False
    elif choice == "%":
        print(num1 % num2)
        pickingOperator = False
    else:
        print("Invalid input")
