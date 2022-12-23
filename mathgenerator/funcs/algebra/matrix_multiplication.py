from ...generator import Generator
from ...latexBuilder import bmatrix
import random


def gen_func(maxVal=100, max_dim=10):
    m = random.randint(2, max_dim)
    n = random.randint(2, max_dim)
    k = random.randint(2, max_dim)

    # generate matrices a and b
    a = [[random.randint(-maxVal, maxVal) for _ in range(n)] for _ in range(m)]
    b = [[random.randint(-maxVal, maxVal) for _ in range(k)] for _ in range(n)]

    res = []
    for r in range(m):
        res.append([])
        for c in range(k):
            temp = 0
            for t in range(n):
                temp += a[r][t] * b[t][c]
            res[r].append(temp)

    problem = f"Multiply ${bmatrix(a)}$ and ${bmatrix(b)}$"
    solution = f'${bmatrix(res)}$'
    return problem, solution


matrix_multiplication = Generator("Multiplication of two matrices", 46,
                                  gen_func,
                                  ["maxVal=100", "max_dim=10"])
