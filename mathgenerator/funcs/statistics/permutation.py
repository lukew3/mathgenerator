from .__init__ import *

import math


def permutationFunc(maxlength=20, format='string'):
    a = random.randint(10, maxlength)
    b = random.randint(0, 9)
    answer = int(math.factorial(a) / (math.factorial(a - b)))

    if format == 'string':
        problem = f"Number of Permutations from {a} objects picked {b} at a time =  "
        solution = str(answer)
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return a, b, answer


permutation = Generator("Permutations", 42, permutationFunc, ["maxlength=20"])
