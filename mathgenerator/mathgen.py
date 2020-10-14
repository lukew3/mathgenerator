import random


class Generator(object):

    """
    Generate variating problems and their solutions based on a given function
    """

    def __init__(self, title, id, generalProb, generalSol, func):
        self.title = title
        self.id = id
        self.generalProb = generalProb
        self.generalSol = generalSol
        self.func = func

    def __str__(self):
        return str(self.id) + " " + self.title + " " + \
            self.generalProb + " " + self.generalSol

    def __call__(self):
        return self.func()


"""
Functions
"""


def additionFunc(maxSum=99, maxAddend=50):
    """Generate a subtraction problem with solution
    :maxSum: the maximum value that can come before the minus sign
    :maxAddend: the maximum difference that has to be calculated
    :returns: an addition problem and solution
    """
    a = random.randint(0, maxAddend)
    # the highest value of b will be no higher than the maxsum minus the first
    # number and no higher than the maxAddend as well
    b = random.randint(0, min((maxSum-a), maxAddend))
    c = a+b
    problem = str(a) + " + " + str(b) + " = "
    solution = str(c)
    return problem, solution


def subtractionFunc(maxMinuend=99, maxDiff=99):
    """Generate a subtraction problem with solution
    :maxMinuend: the maximum value that can come before the minus sign
    :maxDiff: the maximum difference that has to be calculated
    :returns: a subtraction problem and solution
    """
    a = random.randint(0, maxMinuend)
    b = random.randint(max(0, (a-maxDiff)), a)
    c = a-b
    problem = str(a) + " - " + str(b) + " = "
    solution = str(c)
    return problem, solution


"""
Class Instances

Format is:
<title> = Generator("<Title>", <id>, <generalized problem>,
                    <generalized solution>, <function name>)
"""
addition = Generator("Addition", 2, "a + b =", "c", additionFunc)
subtraction = Generator("Subtraction", 3, "a - b =", "c", subtractionFunc)
