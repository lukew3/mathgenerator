from ...generator import Generator
import random


def gen_func(maxVal=10):
    a = random.randint(1, maxVal)
    b = random.randint(1, maxVal)
    c = random.randint(1, maxVal)
    d = random.randint(1, maxVal)

    while (a == b):
        b = random.randint(1, maxVal)

    while (c == d):
        d = random.randint(1, maxVal)

    def calculate_gcd(x, y):
        while (y):
            x, y = y, x % y
        return x

    tmp_n = a * c
    tmp_d = b * d

    gcd = calculate_gcd(tmp_n, tmp_d)

    problem = f"$\\frac{{{a}}}{{{b}}}\\cdot\\frac{{{c}}}{{{d}}}=$"
    if (tmp_d == 1 or tmp_d == gcd):
        solution = f"$\\frac{{{tmp_n}}}{{{gcd}}}$"
    else:
        solution = f"$\\frac{{{tmp_n//gcd}}}{{{tmp_d//gcd}}}$"
    return problem, solution


fraction_multiplication = Generator("Fraction Multiplication", 28,
                                    gen_func, ["maxVal=10"])
