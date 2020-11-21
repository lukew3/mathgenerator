from .__init__ import *


def vectorDotFunc(minVal=-20, maxVal=20):
    a = [random.randint(minVal, maxVal) for i in range(3)]
    b = [random.randint(minVal, maxVal) for i in range(3)]
    c = a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

    problem = str(a) + " . " + str(b) + " = "
    solution = str(c)
    return problem, solution


vector_dot = Generator("Dot Product of 2 Vectors", 72, "a . b = ", "c",
                       vectorDotFunc)
