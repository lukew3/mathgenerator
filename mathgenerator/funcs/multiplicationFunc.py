from .__init__ import *


def multiplicationFunc(maxRes=99, maxMulti=99):
    a = random.randint(0, maxMulti)
    b = random.randint(0, min(int(maxMulti / a), maxRes))
    c = a * b
    
    problem = str(a) + "*" + str(b) + "="
    solution = str(c)
    return problem, solution
