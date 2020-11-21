from .__init__ import *


def combinationsFunc(maxlength=20):
    def factorial(a):
        d = 1
        for i in range(a):
            a = (i + 1) * d
            d = a
        return d

    a = random.randint(10, maxlength)
    b = random.randint(0, 9)

    solution = int(factorial(a) / (factorial(b) * factorial(a - b)))
    problem = "Number of combinations from {} objects picked {} at a time ".format(
        a, b)

    return problem, solution


combinations = Generator(
    "Combinations of Objects", 30,
    "Combinations available for picking 4 objects at a time from 6 distinct objects =",
    " 15", combinationsFunc)
