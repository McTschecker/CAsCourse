import pytest
from multifunctionMathTrainer import createQuestionPM, createQuestionTD, createQuestionPMTD, createQuestionSR

def test_PMBasic ():
    returned =createQuestionPM(1,1,1)
    if  returned == [[1,1,0,2]]:
        assert True
    else:
        assert returned == [[1,1,1,0]]

def test_returnedlenCreateQuestionPM ():
    assert len(createQuestionPM(1, 500000, 10000)) == 10000

def test_TDBasic ():
    returned =createQuestionPM(1,1,1)
    if  returned == [[1,1,0,2]]:
        assert True
    else:
        assert returned == [[1,1,1,0]]

def test_returnedlenCreateQuestionPM ():
    assert len(createQuestionPM(1, 500000, 10000)) == 10000

def test_PMBasic ():
    returned =createQuestionPM(1,1,1)
    if  returned == [[1,1,0,2]]:
        assert True
    else:
        assert returned == [[1,1,1,0]]

def test_returnedlenCreateQuestionPM ():
    assert len(createQuestionPM(1, 500000, 10000)) == 10000

def test_PMBasic ():
    returned =createQuestionPM(1,1,1)
    if  returned == [[1,1,0,2]]:
        assert True
    else:
        assert returned == [[1,1,1,0]]

def test_returnedlenCreateQuestionPM ():
    assert len(createQuestionPM(1, 500000, 10000)) == 10000

def test_PMBasic ():
    returned =createQuestionPM(1,1,1)
    if  returned == [[1,1,0,2]]:
        assert True
    else:
        assert returned == [[1,1,1,0]]

def test_returnedlenCreateQuestionPM ():
    assert len(createQuestionPM(1, 500000, 10000)) == 10000