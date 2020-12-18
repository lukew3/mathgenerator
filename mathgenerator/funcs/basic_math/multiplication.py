from .__init__ import *


def multiplicationFunc(maxRes=99, maxMulti=99, style='raw'):
    a = random.randint(0, maxMulti)
    if a == 0:
        b = random.randint(0, maxRes)
    else:
        b = random.randint(0, min(int(maxMulti / a), maxRes))
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
