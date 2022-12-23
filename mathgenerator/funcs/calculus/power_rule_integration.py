from ...generator import Generator
import random


def gen_func(maxCoef=10,
             maxExp=10,
             maxTerms=5):
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
        solution += f'\\frac{{{coefficient}}}{{{exponent}}}x^{{{exponent + 1}}}'

    solution += " + C"

    return problem + '$', solution + '$'


power_rule_integration = Generator("Power Rule Integration", 48,
                                   gen_func,
                                   ["maxCoef=10", "maxExp=10", "maxTerms=5"])
