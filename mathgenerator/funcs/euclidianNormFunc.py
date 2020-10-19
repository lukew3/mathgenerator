from .__init__ import *


def euclidianNormFunc(v1: list):
    problem = f"Euclidian norm or L2 norm of the vector{v1} is:"
    solution = sqrt(sum([i**2 for i in v1]))
    return problem, solution
