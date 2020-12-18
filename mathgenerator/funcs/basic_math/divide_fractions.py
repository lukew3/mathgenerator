from .__init__ import *


def divideFractionsFunc(maxVal=10, style='raw'):
    a = random.randint(1, maxVal)
    b = random.randint(1, maxVal)

    while (a == b):
        b = random.randint(1, maxVal)

    c = random.randint(1, maxVal)
    d = random.randint(1, maxVal)
    while (c == d):
        d = random.randint(1, maxVal)

    def calculate_gcd(x, y):
        while (y):
            x, y = y, x % y
        return x

    tmp_n = a * d
    tmp_d = b * c

    gcd = calculate_gcd(tmp_n, tmp_d)
    sol_numerator = tmp_n // gcd
    sol_denominator = tmp_d // gcd
    x = f"{sol_numerator}/{sol_denominator}"

    if (tmp_d == 1 or tmp_d == gcd):
        x = f"{sol_numerator}"

    if style == 'latex':
        problem = "\\(\\frac{" + str(a) + "}{" + str(b) + "}\\div\\frac{" + str(c) + "}{" + str(d) + "}=\\)"
        if tmp_d == 1 or tmp_d == gcd:
            solution = "\\(" + str(sol_numerator) + "\\)"
        else:
            solution = "\\(\\frac{" + str(sol_numerator) + "}{" + str(sol_denominator) + "}\\)"
    else:
        problem = f"({a}/{b})/({c}/{d})"
        solution = x
    return problem, solution


divide_fractions = Generator("Fraction Division", 16, "(a/b)/(c/d)=", "x/y",
                             divideFractionsFunc)
