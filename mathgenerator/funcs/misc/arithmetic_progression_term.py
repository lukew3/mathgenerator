from .__init__ import *


def gen_func(maxd=100,
             maxa=100,
             maxn=100,
             format='string'):
    d = random.randint(-1 * maxd, maxd)
    a1 = random.randint(-1 * maxa, maxa)
    a2 = a1 + d
    a3 = a2 + d
    n = random.randint(4, maxn)
    apString = str(a1) + ', ' + str(a2) + ', ' + str(a3) + ' ... '
    solution = a1 + ((n - 1) * d)

    if format == 'string':
        problem = 'Find the term number ' + str(
            n) + ' of the AP series: ' + apString
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return n, apString, solution


arithmetic_progression_term = Generator("AP Term Calculation", 82,
                                        gen_func,
                                        ["maxd=100", "maxa=100", "maxn=100"])
