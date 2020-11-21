from .__init__ import *

import math


def euclidianNormFunc(maxEltAmt=20):
    vec = [
        random.uniform(0, 1000) for i in range(random.randint(2, maxEltAmt))
    ]
    problem = f"Euclidian norm or L2 norm of the vector{vec} is:"
    solution = math.sqrt(sum([i**2 for i in vec]))
    return problem, solution


eucldian_norm = Generator(
    "Euclidian norm or L2 norm of a vector", 69,
    "Euclidian Norm of a vector V:[v1, v2, ......., vn]",
    "sqrt(v1^2 + v2^2 ........ +vn^2)", euclidianNormFunc)
