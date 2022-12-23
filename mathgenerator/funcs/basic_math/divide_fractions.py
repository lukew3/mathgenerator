import random


def divide_fractions(maxVal=10):
    """Divide Fractions"""
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

    return f'$\\frac{{{a}}}{{{b}}}\\div\\frac{{{c}}}{{{d}}}=$', f'$\\frac{{{sol_numerator}}}{{{sol_denominator}}}$'
