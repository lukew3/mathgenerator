from .__init__ import *


def gen_func(maxCoef=10,
             maxExp=10,
             maxTerms=5,
             format='string'):
    numTerms = random.randint(1, maxTerms)
    problem = ""
    solution = ""

    for i in range(numTerms):
        if i > 0:
            problem += " + "
            solution += " + "
        coefficient = random.randint(1, maxCoef)
        exponent = random.randint(1, maxExp)

        problem += str(coefficient) + "x^" + str(exponent)
        solution += "(" + str(coefficient) + "/" + \
            str(exponent) + ")x^" + str(exponent + 1)

    solution += " + c"

    if format == 'string':
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return problem, solution


power_rule_integration = Generator("Power Rule Integration", 48,
                                   gen_func,
                                   ["maxCoef=10", "maxExp=10", "maxTerms=5"])
