from ...generator import Generator
import random
import math


def gen_func(maxCoordinate=20, minCoordinate=-20):
    x1 = random.randint(minCoordinate, maxCoordinate)
    x2 = random.randint(minCoordinate, maxCoordinate)

    y1 = random.randint(minCoordinate, maxCoordinate)
    y2 = random.randint(minCoordinate, maxCoordinate)

    coeff_y = (x2 - x1)
    coeff_x = (y2 - y1)
    constant = y2 * coeff_y - x2 * coeff_x

    gcd = math.gcd(abs(coeff_x), abs(coeff_y))

    if gcd != 1:
        if coeff_y > 0:
            coeff_y //= gcd
        if coeff_x > 0:
            coeff_x //= gcd
        if constant > 0:
            constant //= gcd
        if coeff_y < 0:
            coeff_y = -(-coeff_y // gcd)
        if coeff_x < 0:
            coeff_x = -(-coeff_x // gcd)
        if constant < 0:
            constant = -(-constant // gcd)
    if coeff_y < 0:
        coeff_y = -(coeff_y)
        coeff_x = -(coeff_x)
        constant = -(constant)
    if coeff_x in [1, -1]:
        if coeff_x == 1:
            coeff_x = ''
        else:
            coeff_x = '-'
    if coeff_y in [1, -1]:
        if coeff_y == 1:
            coeff_y = ''
        else:
            coeff_y = '-'

    problem = f"What is the equation of the line between points $({x1},{y1})$ and $({x2},{y2})$ in slope-intercept form?"
    if coeff_x == 0:
        solution = str(coeff_y) + "y = " + str(constant)
    elif coeff_y == 0:
        solution = str(coeff_x) + "x = " + str(-constant)
    else:
        if constant > 0:
            solution = str(coeff_y) + "y = " + str(coeff_x) + "x + " + str(constant)
        else:
            solution = str(coeff_y) + "y = " + str(coeff_x) + "x " + str(constant)
    return problem, f'${solution}$'


equation_of_line_from_two_points = Generator(
    "Equation of line from two points", 114, gen_func,
    ["maxCoordinate=20", "minCoordinate=-20"])
