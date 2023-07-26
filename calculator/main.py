from math_functions import *

def main():
    print("Welcome to the Cadu calculator")
    result = int(input("Enter a number: "))
    end = False
    while not end:
        operator = input("Enter an operator (+, -, *, /, or =): ")
        if(operator == "+"):
            result = sum(result)
        elif(operator == "-"):
            result = sub(result)
        elif(operator == "*"):
            result = mult(result)
        elif(operator == "/"):
            result = div(result)
        elif(operator == "="):
            print(result)
            end = True
        else:
            error()

main()