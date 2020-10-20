from .__init__ import *


def primeFactorsFunc(minVal=1, maxVal=200):
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

    problem = f"Find prime factors of {a}"
    solution = f"{factors}"
    return problem, solution


prime_factors = Generator("Prime Factorisation", 27, "Prime Factors of a =",
                          "[b, c, d, ...]", primeFactorsFunc)
