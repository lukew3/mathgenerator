from .__init__ import *


def subtractionFunc(maxMinuend=99, maxDiff=99, format='string'):
    a = random.randint(0, maxMinuend)
    b = random.randint(max(0, (a - maxDiff)), a)
    c = a - b

    if format == 'string':
        problem = str(a) + "-" + str(b) + "="
        solution = str(c)
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return a, b, c


subtraction = Generator("Subtraction", 1, subtractionFunc,
                        ["maxMinuend=99", "maxDiff=99"])
