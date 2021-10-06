from .__init__ import *


def primeFactorsFunc(minVal=1, maxVal=200, format='string'):
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

    if format == 'string':
        problem = f"Find prime factors of {a}"
        solution = f"{factors}"
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return a, factors


prime_factors = Generator("Prime Factorisation", 27, primeFactorsFunc,
                          ["minVal=1", "maxVal=200"])
