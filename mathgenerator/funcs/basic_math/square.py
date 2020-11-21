from .__init__ import *


def squareFunc(maxSquareNum=20):
    a = random.randint(1, maxSquareNum)
    b = a * a

    problem = str(a) + "^2" + "="
    solution = str(b)
    return problem, solution


square = Generator("Square", 8, "a^2", "b", squareFunc)
