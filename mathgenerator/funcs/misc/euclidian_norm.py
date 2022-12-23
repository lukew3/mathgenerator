import random
import math


def euclidian_norm(maxEltAmt=20):
    """Euclidian norm or L2 norm of a vector"""
    vec = [
        random.uniform(0, 1000) for i in range(random.randint(2, maxEltAmt))
    ]
    solution = round(math.sqrt(sum([i**2 for i in vec])), 2)

    problem = f"Euclidian norm or L2 norm of the vector ${vec}$ is:"
    return problem, f'${solution}$'
