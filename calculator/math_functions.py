def sum(sumNumber):   
    number = int(input("Enter a number: "))
    result = sumNumber + number
    print(f'{sumNumber} + {number} = {result}\n')
    print(f'previous number: {result}')
    return result

def sub( subNumber):    
    number = int(input("Enter a number: "))
    result = subNumber - number
    print(f'{subNumber} - {number} = {result}\n')
    print(f'previous number: {result}')
    return result

def mult(multNumber):  
    number = int(input("Enter a number: "))
    result = multNumber * number
    print(f'{multNumber} * {number} = {result}\n')
    print(f'previous number: {result}')
    return result

def div(divNumber):
    number = int(input("Enter a number: "))
    if number == 0:
        print("Error: Cannot divide by zero.")
        return divNumber
    result = divNumber / number
    print(f'{divNumber} / {number} = {result}\n')
    print(f'previous number: {result}')
    return result

def error():
    print("please, choose a valid option")

