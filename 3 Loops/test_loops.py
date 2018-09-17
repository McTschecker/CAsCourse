import pytest
from Loops import loops

def testFor():
    c,d  = loops()
    c_original = 2
    for i in range(16):
       c_original = c_original * c_original

    assert c == c_original

def testWhile():
    c,d = loops()
    d_original = -155
    while d_original >= 15:
        d_original = d_original + 1
    assert d_original == d