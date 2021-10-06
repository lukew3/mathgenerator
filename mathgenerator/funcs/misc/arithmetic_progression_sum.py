from .__init__ import *


def arithmeticProgressionSumFunc(maxd=100,
                                 maxa=100,
                                 maxn=100,
                                 format='string'):
    d = random.randint(-1 * maxd, maxd)
    a1 = random.randint(-1 * maxa, maxa)
    a2 = a1 + d
    a3 = a1 + 2 * d
    n = random.randint(4, maxn)
    apString = str(a1) + ', ' + str(a2) + ', ' + str(a3) + ' ... '
    an = a1 + (n - 1) * d
    solution = n * (a1 + an) / 2

    if format == 'string':
        problem = 'Find the sum of first ' + \
            str(n) + ' terms of the AP series: ' + apString
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return n, apString, solution


arithmetic_progression_sum = Generator("AP Sum Calculation", 83,
                                       arithmeticProgressionSumFunc,
                                       ["maxd=100", "maxa=100", "maxn=100"])
