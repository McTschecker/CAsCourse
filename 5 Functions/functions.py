### Copyright Fabian Blank
import math as m
## Now you will learn how to use functions in python
## example for hello world
def helloWorld():
    print('Hello World!')

# Now create a function, named "doubleNumber", which doubles a number and then returns it
# Please keep in mind, that the variable given to the Function
def doubleNumber(number):
    try:
        number = float(number)
    except ValueError:
        return None
    return number * 2


# Now create a function, named "rootDouble", which finds the square root of a number and then doubles it. Please then return the final number
def rootDouble(number):
    try:
        number = m.sqrt(number)
        return doubleNumber(number)
    except TypeError:
        return 
