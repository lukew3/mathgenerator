from ...generator import Generator
import random


def gen_func(maxd=100,
             maxa=100,
             maxn=100):
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


arithmetic_progression_sum = Generator("AP Sum Calculation", 83,
                                       gen_func,
                                       ["maxd=100", "maxa=100", "maxn=100"])
