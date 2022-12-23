import random


def arithmetic_progression_sum(maxd=100,
             maxa=100,
             maxn=100):
    """Arithmetic Progression Sum"""
    d = random.randint(-1 * maxd, maxd)
    a1 = random.randint(-1 * maxa, maxa)
    a2 = a1 + d
    a3 = a1 + 2 * d
    n = random.randint(4, maxn)
    apString = str(a1) + ', ' + str(a2) + ', ' + str(a3) + ' ... '
    an = a1 + (n - 1) * d
    solution = n * (a1 + an) / 2

    problem = f'Find the sum of first ${n}$ terms of the AP series: ${apString}$'
    return problem, f'${solution}$'
