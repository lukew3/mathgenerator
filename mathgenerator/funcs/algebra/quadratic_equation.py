from .__init__ import *

import math


def gen_func(maxVal=100, format='string'):
    a = random.randint(1, maxVal)
    c = random.randint(1, maxVal)
    b = random.randint(
        round(math.sqrt(4 * a * c)) + 1, round(math.sqrt(4 * maxVal * maxVal)))
    D = math.sqrt(b * b - 4 * a * c)
    res = [round((-b + D) / (2 * a), 2), round((-b - D) / (2 * a), 2)]

    if format == 'string':
        problem = "Zeros of the Quadratic Equation {}x^2+{}x+{}=0".format(
            a, b, c)
        solution = str(res)
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return a, b, c, res


quadratic_equation = Generator("Quadratic Equation", 50, gen_func,
                               ["maxVal=100"])
