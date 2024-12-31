# Calculator using python having basic 5 operators (+,-,*,/,%)

while True:
    temp = 0
    operator = input("\n\n"+"--"*35+"\nEnter operator: \n1. +\n2. -\n3. *\n4. / \n5. % \n6. Close\n>>")
    
    if operator.lower() == "close":
        break

    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))

    if operator == "+":
        print(a+b)
    elif operator == "-":
        print(a-b)
    elif operator == "*":
        print(a*b)
    elif operator == "/":
        print(a/b)
    elif operator == "%":
        print(a%b)
    else:
        print("Invalid operator. Try again")