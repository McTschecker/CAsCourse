import pytest
from variables import variables

def test_multiply():
    aInt, bInt, aString, bString, helloWorld, multiply, power, fitInto = variables()
    assert multiply == aInt * bInt

def test_addString():
    aInt, bInt, aString, bString, helloWorld, multiply, power, fitInto = variables()
    assert helloWorld == aString + bString

def test_power():
    aInt, bInt, aString, bString, helloWorld, multiply, power, fitInto = variables()
    assert power == bInt ** aInt

def test_devide():
    aInt, bInt, aString, bString, helloWorld, multiply, power, fitInto = variables()
    assert fitInto == bInt / aInt