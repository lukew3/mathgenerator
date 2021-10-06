from .__init__ import *


def combinationsFunc(maxlength=20, format='string'):
    def factorial(a):
        d = 1
        for i in range(a):
            a = (i + 1) * d
            d = a
        return d

    a = random.randint(10, maxlength)
    b = random.randint(0, 9)

    solution = int(factorial(a) / (factorial(b) * factorial(a - b)))

    if format == 'string':
        problem = f"Number of combinations from {a} objects picked {b} at a time "
        return problem, str(solution)
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return a, b, solution


combinations = Generator("Combinations of Objects", 30, combinationsFunc,
                         ["maxlength=20"])
