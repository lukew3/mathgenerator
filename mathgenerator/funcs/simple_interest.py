from .__init__ import *


def simpleInterestFunc(maxPrinciple=10000, maxRate=10, maxTime=10):
    a = random.randint(1000, maxPrinciple)
    b = random.randint(1, maxRate)
    c = random.randint(1, maxTime)
    d = (a * b * c) / 100

    problem = "Simple interest for a principle amount of " + str(
        a) + " dollars, " + str(
            b) + "% rate of interest and for a time period of " + str(
                c) + " years is = "
    solution = round(d, 2)
    return problem, solution


simple_interest = Generator(
    "Simple Interest", 45,
    "Simple interest for a principle amount of a dollars, b% rate of interest and for a time period of c years is = ",
    "d dollars", simpleInterestFunc)
