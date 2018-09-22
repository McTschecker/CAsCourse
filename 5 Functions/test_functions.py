### Copyright Fabian Blank
from functions import doubleNumber, rootNumber


def testDoubleNumber0():
    assert doubleNumber(0) == 0, 'Learn maths'
    
def testDoubleNumber1():
    assert doubleNumber(15) == 30, 'Learn maths'

def testDoubleNumber2():
    assert doubleNumber(8888888888) == 17777777776, 'Are you sure this is calculated right? Or are you overflowing?'

def testDoubleNumberWithString():
    assert doubleNumber('HAHA') == None , "Check your input"

### Def test square root of number and then double
def testSquareDoule1():
    assert rootNumber(81) == 18, 'Check your maths'

def testSquareDoule2():
    assert rootNumber(39506172831604938272) == 17777777777, 'Check your function for errors'

def testNumberLikeAnAsshole():
    assert rootNumber('hjfajkldsfakljödsfakljödsfajkldsfjklsfdgjklfdgjklfdgjklg') == None, 'I know you hate me now, but check the users input'
