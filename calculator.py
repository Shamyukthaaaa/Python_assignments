#Design a calculator
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
sum="+"
difference="-"
product="*"
division="/"
floor_division="//"
exponentiation="**"
trial=0
while(trial<3):
    calculate=input("Enter an operator: ")
    if(calculate== "+"):
        addition= num1 + num2
        print(f"The sum of {num1} and {num2} is:",addition)
    elif(calculate=="-"):
        subtraction= num1 - num2
        print(f"The difference of {num1} and {num2} is:",subtraction)
    elif(calculate=="*"):
        multiplication= num1 * num2
        print(f"The product of {num1} and {num2} is:",multiplication)
    elif(calculate=="/"):
        divide= num1 / num2
        print(f"The division of {num1} and {num2} is:",divide)
    elif(calculate=="//"):
        floor_div= num1 // num2
        print(f"The floor division of {num1} and {num2} is:",floor_div)
    elif(calculate=="**"):
        power= num1 ** num2
        print(f"The exponentiation of {num1} and {num2} is:",power)
    else:
        print("Enter a valid operator")
    trial+=1

    


