from .__init__ import *


def gen_func(maxPrinciple=10000,
                       maxRate=10,
                       maxTime=10,
                       format='string'):
    a = random.randint(1000, maxPrinciple)
    b = random.randint(1, maxRate)
    c = random.randint(1, maxTime)
    d = round((a * b * c) / 100, 2)

    if format == 'string':
        problem = "Simple interest for a principle amount of " + str(
            a) + " dollars, " + str(
                b) + "% rate of interest and for a time period of " + str(
                    c) + " years is = "
        solution = str(d)
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return a, b, c, d


simple_interest = Generator("Simple Interest", 45, gen_func,
                            ["maxPrinciple=10000", "maxRate=10", "maxTime=10"])
