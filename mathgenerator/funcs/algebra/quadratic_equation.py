from .__init__ import *

import math


def quadraticEquation(maxVal=100):
    a = random.randint(1, maxVal)
    c = random.randint(1, maxVal)
    b = random.randint(
        round(math.sqrt(4 * a * c)) + 1, round(math.sqrt(4 * maxVal * maxVal)))

    problem = "Zeros of the Quadratic Equation {}x^2+{}x+{}=0".format(a, b, c)
    D = math.sqrt(b * b - 4 * a * c)
    solution = str(
        [round((-b + D) / (2 * a), 2),
         round((-b - D) / (2 * a), 2)])
    return problem, solution


quadratic_equation = Generator(
    "Quadratic Equation", 50,
    "Find the zeros {x1,x2} of the quadratic equation ax^2+bx+c=0", "x1,x2",
    quadraticEquation)
