from .__init__ import *


def gen_func(maxVal=20, format='string'):
    a = random.randint(1, maxVal)
    b = random.randint(1, maxVal)
    c = a * b
    x, y = a, b

    while y:
        x, y = y, x % y
    d = c // x

    if format == 'string':
        problem = f"LCM of {a} and {b} ="
        solution = str(d)
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return a, b, d


lcm = Generator("LCM (Least Common Multiple)", 9, gen_func, ["maxVal=20"])
