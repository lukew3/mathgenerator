from .__init__ import *


def gen_func(maxVal=20, format='string'):
    a = random.randint(1, maxVal)
    b = random.randint(1, maxVal)
    x, y = a, b
    while (y):
        x, y = y, x % y

    if format == 'string':
        problem = f"HCF of {a} and {b} = "
        solution = str(x)
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return a, b, x


hcf = Generator("HCF (Highest Common Factor)", 51, gen_func, ["maxVal=20"])
