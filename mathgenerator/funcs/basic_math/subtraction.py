from .__init__ import *


def subtractionFunc(maxMinuend=99, maxDiff=99):
    a = random.randint(0, maxMinuend)
    b = random.randint(max(0, (a - maxDiff)), a)
    c = a - b

    problem = str(a) + "-" + str(b) + "="
    solution = str(c)
    return problem, solution


subtraction = Generator("Subtraction", 1, "a-b=", "c", subtractionFunc)
