from .__init__ import *


def euclidianNormFunc(maxEltAmt=20):
    vec = [random.uniform(0, 1000) for i in range(random.randint(2, maxEltAmt))]
    problem = f"Euclidian norm or L2 norm of the vector{vec} is:"
    solution = math.sqrt(sum([i**2 for i in vec]))
    return problem, solution
