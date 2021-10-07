from .__init__ import *


def gen_func(maxMulti=12, format='string'):
    a = random.randint(0, maxMulti)
    b = random.randint(0, maxMulti)
    c = a * b

    if format == 'string':
        problem = str(a) + "*" + str(b) + "="
        solution = str(c)
        return problem, solution
    elif format == 'latex':
        problem = "\\(" + str(a) + "\\cdot" + str(b) + "=\\)"
        solution = "\\(" + str(c) + "\\)"
    else:
        return a, b, c


multiplication = Generator("Multiplication", 2, gen_func,
                           ["maxMulti=12"])
