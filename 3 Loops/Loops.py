### Copyright Fabian Blank
def loops():
    ### In this chapter we are going to learn loops 
    ### Loops are an esential Part of programming

    # There are 2 Types of loops

    ## For loop
    # The format of a for loop is as follows 
    # for boolean statement
    # the boolean statement can be itterating through a number or array
    # example
    for i in range(15): #goes upto 14
        print (i) #Outputs numbers from 1 to 14

    # Now try iterating so that the variable c is multiplied by itself 15 times
    c = 2
    for u in range(16):
        c = c * c
    # a while statement may be used to wait for a certain thing to be true
    a = 1 
    while a != 2:
        a = 2
        print("A is now equal to 2")

    # Now try adding 1 to d until d is equal to 15
    d = -155
    while d >= 15:
        d = d + 1

    return c, d