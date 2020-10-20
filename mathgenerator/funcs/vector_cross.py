from .__init__ import *


def vectorCrossFunc(minVal=-20, maxVal=20):
    a = [random.randint(minVal, maxVal) for i in range(3)]
    b = [random.randint(minVal, maxVal) for i in range(3)]
    c = [
        a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0]
    ]

    problem = str(a) + " X " + str(b) + " = "
    solution = str(c)
    return problem, solution


vector_cross = Generator("Cross Product of 2 Vectors", 43, "a X b = ", "c",
                         vectorCrossFunc)
