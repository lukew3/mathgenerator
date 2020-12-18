from .__init__ import *


def multiplyFractionsFunc(maxVal=10, style='raw'):
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
    x = f"{tmp_n//gcd}/{tmp_d//gcd}"

    if (tmp_d == 1 or tmp_d == gcd):
        x = f"{tmp_n//gcd}"

    if style == 'latex':
        problem = f"\\(\\frac{{{a}}}{{{b}}}\\cdot\\frac{{{c}}}{{{d}}}=\\)"
        if (tmp_d == 1 or tmp_d == gcd):
            solution = f"\\(\\frac{{{tmp_n}}}{{{gcd}}}\\)"
        else:
            solution = f"\\(\\frac{{{tmp_n//gcd}}}{{{tmp_d//gcd}}}\\)"
    else:
        problem = f"({a}/{b})*({c}/{d})"
        solution = x
    return problem, solution


fraction_multiplication = Generator("Fraction Multiplication", 28,
                                    "(a/b)*(c/d)=", "x/y",
                                    multiplyFractionsFunc)
