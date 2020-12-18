from .__init__ import *


def complexDivisionFunc(maxRes=99, maxDivid=99, style='raw'):
    a = random.randint(0, maxDivid)
    b = random.randint(1, min(maxRes, maxDivid))
    c = a / b
    c = round(c, 2)

    if style == 'latex':
        problem = "\\(" + str(a) + "\\div" + str(b) + "=\\)"
        solution = "\\(" + str(c) + "\\)"
    else:
        problem = str(a) + "/" + str(b) + "="
        solution = str(c)
    return problem, solution


complex_division = Generator("Complex Division", 13, "a/b=", "c", complexDivisionFunc)
