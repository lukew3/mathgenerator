from .__init__ import *


def gen_func(maxBase=3, maxVal=8, format='string'):
    a = random.randint(1, maxVal)
    b = random.randint(2, maxBase)
    c = pow(b, a)

    if format == 'string':
        problem = "log" + str(b) + "(" + str(c) + ")"
        solution = str(a)
        return problem, solution
    elif format == 'latex':
        problem = "\\(\\log_{" + str(b) + "}" + str(c) + "\\)"
        solution = "\\(" + str(a) + "\\)"
        return problem, solution
    else:
        return b, c, a


log = Generator("Logarithm", 12, gen_func, ["maxBase=3", "maxVal=8"])
