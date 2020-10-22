from .__init__ import *


def powerRuleDifferentiationFunc(maxCoef=10, maxExp=10, maxTerms=5):
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
        solution += str(coefficient * exponent) + "x^" + str(exponent - 1)
    return problem, solution


power_rule_differentiation = Generator("Power Rule Differentiation", 7,
                                       "nx^m=", "(n*m)x^(m-1)",
                                       powerRuleDifferentiationFunc)
