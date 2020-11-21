from .__init__ import *

import math


def nthFibonacciNumberFunc(maxN=100):
    golden_ratio = (1 + math.sqrt(5)) / 2
    n = random.randint(1, maxN)
    problem = f"What is the {n}th Fibonacci number?"
    ans = round((math.pow(golden_ratio, n) - math.pow(-golden_ratio, -n)) / (math.sqrt(5)))
    solution = f"{ans}"
    return problem, solution


nth_fibonacci_number = Generator("nth Fibonacci number", 62,
                                 "What is the nth Fibonacci number", "Fn",
                                 nthFibonacciNumberFunc)
