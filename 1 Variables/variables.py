### Copyright Fabian Blank
def variables():
    ### In this chapter you will learn how to manipulate variables
    ### For this you will need to know how to maipulate strings, numbers

    ### Let's start by creating some variables
    ## Numbers
    # You can assign numbers to variables by doign variable = newValue
    # In python previously assigned variables can accept a different type
    aInt = 12
    bInt = 123

    ## Strings
    # To assign strings you will need to do this: variable = 'new value' 
    # it will also work with " instead of '
    aString = 'Hello'
    bString = 'World!'

    # Variables can be added or subtracted as follow
    print(aInt - bInt)
    
    # Use this knowledge to make Hello World only from the definded variables  
    helloWorld = aString + bString
    # Try multiplying aInt by bInt
    multiply = aInt * bInt

    #Try taking bInt to the power of aInt
    power = bInt ** aInt
    # How often does aInt fit in bInt
    fitInto = bInt / aInt


    #Ignore for now:
    return aInt, bInt, aString, bString, helloWorld, multiply, power, fitInto
