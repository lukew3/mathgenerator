from .__init__ import *


def moduloFunc(maxRes=99, maxModulo=99):
    a = random.randint(0, maxModulo)
    b = random.randint(0, min(maxRes, maxModulo))
    c = a % b
    
    problem = str(a) + "%" + str(b) + "="
    solution = str(c)
    return problem, solution
