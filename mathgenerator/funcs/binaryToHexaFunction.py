from .__init__ import *


def binaryToHexaFunc(max_dig=1000):
    problem = ''
    for i in range(random.randint(1, max_dig)):
        temp = str(random.randint(0, 1))
        problem += temp

    solution = hex(int(problem))
    return problem, solution
