import random

def addition(maxSum, maxAddend):
    """
    DESCRIPTION:
        Generates addition problems with positive addends less than maxAddend and sum less than maxSum
    SKILLID:
        2
    PROBLEM:
        "a+b="
    SOLUTION:
        "c"
    """
    a = random.randint(0, maxAddend)
    b = random.randint(0, min((maxSum-a), maxAddend)) #The highest value of b will be no higher than the maxsum minus the first number and no higher than the maxAddend as well
    c = a+b
    problem = str(a) + "+" + str(b) + "="
    solution = str(c)
    return problem, solution

def subtraction(maxDiff, maxMinuend):
    """
    DESCRIPTION:
        Generates subtraction problems with difference between 0 and maxDiff. Minuend and subtrahend are between 0 and maxMinuend.
    SKILLID:
        3
    PROBLEM:
        "a-b="
    SOLUTION:
        "c"
    """
    a = random.randint(0, maxMinuend)
    b = random.randint(max(0, (a-maxDiff)), a)
    c = a-b
    problem = str(a) + "-" + str(b) + "="
    solution = str(c)
    return problem, solution
