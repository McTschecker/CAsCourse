### Copyright Adren Poulard

## You will now learn how to use if, else & elif statements in Python

##If & else statements

print("Do you like cheese?")
Question = input()

#Make input all lowercase
Question = (Question.lower())

#If a, do b. Else, do c.
if Question == "yes":
    print("Cool")
else:
    print("Oh no")

##Elif statements

print("Do you like bread?")
Question2 = input()

#Make input all lowercase
Question2 = (Question2.lower())

#If a, do b. Else if c, do d. Else, do e.
if Question2 == "yes":
    print("Yay")

elif Question2 == "maybe":
    print("Oh")
else:
    print(":(")


##Create your own text-based game/adventure using if, else & elif statements
##Use at least two if statements, one else statement, and one elif statement
##Tip: You can have statements within statements!


