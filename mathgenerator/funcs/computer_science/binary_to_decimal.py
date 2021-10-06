from .__init__ import *


def binaryToDecimalFunc(max_dig=10, format='string'):
    problem = ''

    for i in range(random.randint(1, max_dig)):
        temp = str(random.randint(0, 1))
        problem += temp

    if format == 'string':
        solution = int(problem, 2)
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return problem, solution


binary_to_decimal = Generator("Binary to Decimal", 15, binaryToDecimalFunc,
                              ["max_dig=10"])
