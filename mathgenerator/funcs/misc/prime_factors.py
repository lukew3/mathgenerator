from ...generator import Generator
import random


def gen_func(minVal=1, maxVal=200):
    a = random.randint(minVal, maxVal)
    n = a
    i = 2
    factors = []

    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)

    if n > 1:
        factors.append(n)

    problem = f"Find prime factors of ${a}$"
    solution = f"${', '.join(map(str, factors))}$"
    return problem, solution


prime_factors = Generator("Prime Factorisation", 27, gen_func,
                          ["minVal=1", "maxVal=200"])
