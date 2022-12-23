import random


def power_rule_differentiation(maxCoef=10,
             maxExp=10,
             maxTerms=5):
    """Power Rule Differentiation"""
    numTerms = random.randint(1, maxTerms)
    problem = "$"
    solution = "$"

    for i in range(numTerms):
        if i > 0:
            problem += " + "
            solution += " + "
        coefficient = random.randint(1, maxCoef)
        exponent = random.randint(1, maxExp)

        problem += f'{coefficient}x^{{{exponent}}}'
        solution += f'{coefficient * exponent}x^{{{exponent - 1}}}'

    return problem + '$', solution + '$'
