### Coperationyright Fabian Blank
### In thic chapter we will build a math trainer
import random
from decimal import Decimal, getcontext
getcontext().prec = 2
def trainMath (iterations, min, max, test = False):
    ### You will get the following variables
    ### iterations - number of questions
    ### min - minimum number 
    ### max - maximum number
    
    # You will need some randomness and then find numbers 
    numbers = []
    for i in range(iterations + 1):
        number1 = Decimal(random.randint(min, max ))
        number2 = Decimal(random.randint(min, max ))
        operation = random.randint(1,4) 
        result = 0
        if operation == 1:
            result = number1 + number2
        elif operation == 2:
            result = number1 - number2
        elif operation == 3:
            result = number1 * number2
        elif operation == 4:
            result = number1 / number2
        result = Decimal(result)
        calc = [number1, operation, number2, result]
        numbers = numbers + [calc]
       # print (numbers)

    ### output numbers 

    ### Return numbers as an 2D array of form
    ### [[number 1, operationeration, number 2, Solution] ...]
    
    ### + 0
    ### - 1
    ### * 3
    ### / 4
    if test:
        return numbers 
    else:
        for operation in numbers:
            n1 = operation[0]
            op = operation[1]
            n2 = operation[2]
            actual = Decimal(operation[3])
            if op == 1:
                print("What is", n1, " + ", n2)
            elif op == 2:
                print("What is", n1, " - ", n2)
            elif op == 3:
                print("What is", n1, " * ", n2)
            elif op == 4:
                print("What is", n1, " / ", n2, "To the first 2 significant figures")
            userInput = input()
            try:
                userInput = float(userInput)
                userInput = Decimal(userInput)
            except ValueError:
                print("Invalid input")
            if userInput == actual:
                print("That is correct")
            else:
                print("That is not correct! YOU SUCK!!!! The correct result would be", actual)
          


trainMath(5,1,100, test=False)