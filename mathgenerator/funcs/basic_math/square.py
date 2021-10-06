from .__init__ import *


def squareFunc(maxSquareNum=20, format='string'):
    a = random.randint(1, maxSquareNum)
    b = a * a

    if format == 'string':
        problem = str(a) + "^2" + "="
        solution = str(b)
        return problem, solution
    if format == 'latex':
        problem = "\\(" + str(a) + "^{2}=\\)"
        solution = "\\(" + str(b) + "\\)"
        return problem, solution
    else:
        return a, b


square = Generator("Square", 8, squareFunc, ["maxSquareNum=20"])
