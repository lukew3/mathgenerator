from .__init__ import *


def logFunc(maxBase=3, maxVal=8, style='raw'):
    a = random.randint(1, maxVal)
    b = random.randint(2, maxBase)
    c = pow(b, a)

    if style == 'latex':
        problem = "\\(\\log_{" + str(b) + "}" + str(c) + "\\)"
        print(problem)
        solution = "\\(" + str(a) + "\\)"
    else:
        problem = "log" + str(b) + "(" + str(c) + ")"
        solution = str(a)

    return problem, solution


log = Generator("Logarithm", 12, "log2(8)", "3", logFunc)
