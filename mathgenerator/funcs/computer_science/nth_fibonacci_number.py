from .__init__ import *

import math


def nthFibonacciNumberFunc(maxN=100, format='string'):
    golden_ratio = (1 + math.sqrt(5)) / 2
    n = random.randint(1, maxN)
    problem = f"What is the {n}th Fibonacci number?"
    ans = int((math.pow(golden_ratio, n) - math.pow(-golden_ratio, -n)) / (math.sqrt(5)))

    if format == 'string':
        return problem, str(ans)
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return n, ans


nth_fibonacci_number = Generator("nth Fibonacci number", 62,
                                 nthFibonacciNumberFunc, ["maxN=100"])
