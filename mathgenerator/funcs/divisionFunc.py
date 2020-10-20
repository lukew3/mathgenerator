from .__init__ import *
from ..__init__ import Generator


def divisionFunc(maxRes=99, maxDivid=99):
    a = random.randint(0, maxDivid)
    b = random.randint(0, min(maxRes, maxDivid))
    c = a / b

    problem = str(a) + "/" + str(b) + "="
    solution = str(c)
    return problem, solution


division = Generator("Division", 3, "a/b=", "c", divisionFunc)
