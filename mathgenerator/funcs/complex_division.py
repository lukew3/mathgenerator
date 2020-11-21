from .__init__ import *


def complexDivisionFunc(maxRes=99, maxDivid=99):
    a = random.randint(0, maxDivid)
    b = random.randint(0, min(maxRes, maxDivid))
    c = a / b
    c = round(c, 2)

    problem = str(a) + "/" + str(b) + "="
    solution = str(c)
    return problem, solution


complex_division = Generator("Complex Division", 13, "a/b=", "c", complexDivisionFunc)
