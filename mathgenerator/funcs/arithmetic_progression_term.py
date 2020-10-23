from .__init__ import *


def arithmeticProgressionTermFunc(maxd=100, maxa=100, maxn=100):
    d = random.randint(-1 * maxd, maxd)
    a1 = random.randint(-1 * maxa, maxa)
    a2 = a1 + d
    a3 = a2 + d
    n = random.randint(4, maxn)
    apString = str(a1) + ', ' + str(a2) + ', ' + str(a3) + ' ... '
    problem = 'Find the term number ' + str(
        n) + ' of the AP series: ' + apString
    solution = a1 + ((n - 1) * d)
    return problem, solution


arithmetic_progression_term = Generator(
    "AP Term Calculation", 82,
    "Find the term number n of the AP series: a1, a2, a3 ...", "a-n",
    arithmeticProgressionTermFunc)
