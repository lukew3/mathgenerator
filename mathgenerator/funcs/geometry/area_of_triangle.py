from .__init__ import *


def areaOfTriangleFunc(maxA=20, maxB=20, maxC=20):
    a = random.randint(1, maxA)
    b = random.randint(1, maxB)
    c = random.randint(1, maxC)

    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c))**0.5

    problem = "Area of triangle with side lengths: " + \
        str(a) + " " + str(b) + " " + str(c) + " = "
    solution = str(area)
    return problem, solution


area_of_triangle = Generator("Area of Triangle", 18,
                             "Area of Triangle with side lengths a, b, c = ",
                             "area", areaOfTriangleFunc)
