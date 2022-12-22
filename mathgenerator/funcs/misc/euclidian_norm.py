from ...generator import Generator
import random
import math


def gen_func(maxEltAmt=20):
    vec = [
        random.uniform(0, 1000) for i in range(random.randint(2, maxEltAmt))
    ]
    solution = round(math.sqrt(sum([i**2 for i in vec])), 2)

    problem = f"Euclidian norm or L2 norm of the vector ${vec}$ is:"
    return problem, f'${solution}$'


euclidian_norm = Generator("Euclidian norm or L2 norm of a vector", 69,
                           gen_func, ["maxEltAmt=20"])
