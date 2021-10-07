from .__init__ import *


def gen_func(minVal=-20, maxVal=20, format='string'):
    a = [random.randint(minVal, maxVal) for i in range(3)]
    b = [random.randint(minVal, maxVal) for i in range(3)]
    c = [
        a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0]
    ]

    if format == 'string':
        problem = str(a) + " X " + str(b) + " = "
        solution = str(c)
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return a, b, c


vector_cross = Generator("Cross Product of 2 Vectors", 43, gen_func,
                         ["minVal=-20", "maxVal=20"])
