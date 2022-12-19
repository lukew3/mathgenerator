from ...__init__ import Generator
import random
import math


def gen_func(maxN=100, format='string'):
    gratio = (1 + math.sqrt(5)) / 2
    n = random.randint(1, maxN)
    problem = f"What is the {n}th Fibonacci number?"
    ans = int((math.pow(gratio, n) - math.pow(-gratio, -n)) / (math.sqrt(5)))

    if format == 'string':
        return problem, str(ans)
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return n, ans


nth_fibonacci_number = Generator("nth Fibonacci number", 62,
                                 gen_func, ["maxN=100"])
