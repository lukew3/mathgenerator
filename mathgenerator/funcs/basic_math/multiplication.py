from .__init__ import *


def multiplicationFunc(maxMulti=12, style='raw'):
    a = random.randint(0, maxMulti)
    b = random.randint(0, maxMulti)
    c = a * b

    if style == 'latex':
        problem = "\\(" + str(a) + "\\cdot" + str(b) + "=\\)"
        solution = "\\(" + str(c) + "\\)"
    else:
        problem = str(a) + "*" + str(b) + "="
        solution = str(c)
    return problem, solution


multiplication = Generator("Multiplication", 2, "a*b=", "c",
                           multiplicationFunc)
