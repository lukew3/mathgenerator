from ...__init__ import Generator
import random


def gen_func(maxNum=250, format='string'):
    a = random.randint(2, maxNum)

    problem = f"Is {a} composite?"
    if a == 0 or a == 1:
        solution = "No"
        return (problem, solution)
    for i in range(2, a):
        if a % i == 0:
            solution = "Yes"
            return (problem, solution)
    solution = "No"

    if format == 'string':
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return a, solution


is_composite = Generator('Is Composite', 124, gen_func, ["maxNum=250"])
