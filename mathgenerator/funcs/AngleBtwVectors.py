import eucldianNorm
import math
from .__init__ import *


def AngleBtwVectors(v1: list, v2: list):
    sum = 0
    for i in v1:
        for j in v2:
            sum += i * j

    mags = euclidianNorm(v1) * euclidianNorm(v2)
    problem = f"angle between the vectors {v1} and {v2} is:"
    solution = math.acos(sum / mags)
    # would return the answer in radians
    return problem, solution
