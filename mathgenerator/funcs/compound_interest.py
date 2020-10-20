from .__init__ import *


def compoundInterestFunc(maxPrinciple=10000,
                         maxRate=10,
                         maxTime=10,
                         maxPeriod=10):
    p = random.randint(100, maxPrinciple)
    r = random.randint(1, maxRate)
    t = random.randint(1, maxTime)
    n = random.randint(1, maxPeriod)
    A = p * ((1 + (r / (100 * n))**(n * t)))
    problem = "Compound Interest for a principle amount of " + str(
        p) + " dollars, " + str(
            r) + "% rate of interest and for a time period of " + str(
                t) + " compounded monthly is = "
    solution = round(A, 2)
    return problem, solution


compound_interest = Generator(
    "Compound Interest", 78,
    "Compound interest for a principle amount of p dollars, r% rate of interest and for a time period of t years with n times compounded annually is = ",
    "A dollars", compoundInterestFunc)
