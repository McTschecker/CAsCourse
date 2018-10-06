# This script writes tests for the multi math trainer
import string, random, os
ranges = []
Sol = []
function = 'createQuestionPM'

def generateRanges(high, low, changeHi):
    ranges = []
    i = low
    steps = 0
    hi = low
    for i in range(high):
        steps *= 1
        hi = float( hi * changeHi)
        ranges += [[low, hi]]
    return ranges

def generataAmountSloutions(high, low):
    i = low
    solutions = []
    while i < high:
        solutions += [i]
        i += 1
    return solutions

def printTests(function, ranges, amountSolutions):
    tests = '' 
    print(len(ranges))
    print(len(amountSolutions))
    for rangeq  in ranges:
        for solution in amountSolutions:
            tests += 'def test'
            tests += ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=15))
            tests += '():' 
            tests += os.linesep
            tests +='   assert len('
            tests += str(function)
            tests += '('
            tests += str(solution)
            tests += ','
            tests += tests.join([str(rangeq)])
            tests += ')) == '
            tests += str(solution)
            tests += os.linesep
            #tests += 'def test', str(rangeq), str(solution), '():  \n  assert len(', str(function), '(', str(solution), ', ' , str(''.join(rangeq)), ') == len(', str(solution) ,')'
    return tests

tests = printTests(function, generateRanges(100, 50, 1.2), generataAmountSloutions(50, 10))

out = open('tests.py', 'w')
out.write(tests)