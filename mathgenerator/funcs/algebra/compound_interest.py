from .__init__ import *


def compoundInterestFunc(maxPrinciple=10000, maxRate=10, maxTime=10):
    p = random.randint(1000, maxPrinciple)
    r = random.randint(1, maxRate)
    n = random.randint(1, maxTime)
    a = p * (1 + r / 100)**n
    problem = "Compound interest for a principle amount of " + \
        str(p) + " dollars, " + str(r) + \
        "% rate of interest and for a time period of " + str(n) + " year is = "
    solution = round(a, 2)
    return problem, solution


compound_interest = Generator(
    "Compound Interest", 78,
    "Compound interest for a principle amount of a dollars, b% rate of interest and for a time period of c years is = ",
    "d dollars", compoundInterestFunc)
