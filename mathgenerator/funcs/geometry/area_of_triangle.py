from ...__init__ import Generator
import random


def gen_func(maxA=20, maxB=20, format='string'):
    a = random.randint(1, maxA)
    b = random.randint(1, maxB)
    c = random.randint(abs(b - a) + 1, abs(a + b) - 1)

    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c))**0.5

    if format == 'string':
        problem = "Area of triangle with side lengths: " + \
            str(a) + " " + str(b) + " " + str(c) + " = "
        solution = str(round(area, 2))
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return a, b, c, area


area_of_triangle = Generator("Area of Triangle", 18, gen_func,
                             ["maxA=20", "maxB=20"])
