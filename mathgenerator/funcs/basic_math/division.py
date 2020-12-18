from .__init__ import *


def divisionToIntFunc(maxA=25, maxB=25, style='raw'):
    a = random.randint(1, maxA)
    b = random.randint(1, maxB)

    divisor = a * b
    dividend = random.choice([a, b])
    quotient = int(divisor / dividend)

    if style == 'latex':
        problem = "\\(" + str(divisor) + "\\div" + str(dividend) + "=\\)"
        solution = "\\(" + str(quotient) + "\\)"
    else:
        problem = f"{divisor}/{dividend}="
        solution = str(quotient)
    return problem, solution


division = Generator("Division", 3, "a/b=", "c", divisionToIntFunc)
