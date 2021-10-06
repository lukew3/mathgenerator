from .__init__ import *


def compoundInterestFunc(maxPrinciple=10000,
                         maxRate=10,
                         maxTime=10,
                         format='string'):
    p = random.randint(1000, maxPrinciple)
    r = random.randint(1, maxRate)
    n = random.randint(1, maxTime)
    a = round(p * (1 + r / 100)**n, 2)

    if format == 'string':
        problem = "Compound interest for a principle amount of " + \
            str(p) + " dollars, " + str(r) + \
            "% rate of interest and for a time period of " + str(n) + " year is = "
        return problem, str(a)
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return p, r, n, a


compound_interest = Generator(
    "Compound Interest", 78, compoundInterestFunc,
    ["maxPrinciple=10000", "maxRate=10", "maxTime=10"])
