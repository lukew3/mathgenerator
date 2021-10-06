from .__init__ import *
import random


def signumFunc(min=-999, max=999, format='string'):
    a = random.randint(min, max)
    b = 0
    if (a > 0):
        b = 1
    if (a < 0):
        b = -1

    if format == 'string':
        problem = "signum of " + str(a) + " is " + "="
        solution = str(b)
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return a, b


signum_function = Generator("signum function", 106, signumFunc,
                            ["min=-999", "max=999"])
