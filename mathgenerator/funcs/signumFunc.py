from .__init__ import *
import random


def signumFunc(min=-999, max=999):
    a = random.randint(min, max)
    b = 0
    if (a > 0):
        b = 1
    if (a < 0):
        b = -1
    problem = "signum of " + str(a) + " is " + "="
    solution = str(b)
    return problem, solution


signum_function = Generator("signum function", 106,
                            "signum function of a is", "b",
                            signumFunc)
