from .__init__ import *


def squareFunc(maxSquareNum=20, style='raw'):
    a = random.randint(1, maxSquareNum)
    b = a * a

    if style == 'latex':
        problem = "\\(" + str(a) + "^{2}=\\)"
        solution = "\\(" + str(b) + "\\)"
    else:
        problem = str(a) + "^2" + "="
        solution = str(b)
    return problem, solution


square = Generator("Square", 8, "a^2", "b", squareFunc)
