from .__init__ import *
from ..__init__ import Generator


def absoluteDifferenceFunc(maxA=100, maxB=100):
    a = random.randint(-1 * maxA, maxA)
    b = random.randint(-1 * maxB, maxB)
    absDiff = abs(a - b)

    problem = "Absolute difference between numbers " + \
        str(a) + " and " + str(b) + " = "
    solution = absDiff
    return problem, solution


absoluteDifference = Generator(
    "Absolute difference between two numbers", 71,
    "Absolute difference betweeen two numbers a and b =", "|a-b|",
    absoluteDifferenceFunc)
