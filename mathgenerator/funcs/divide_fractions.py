from .__init__ import *


def divideFractionsFunc(maxVal=10):
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
    x = f"{tmp_n//gcd}/{tmp_d//gcd}"

    if (tmp_d == 1 or tmp_d == gcd):
        x = f"{tmp_n//gcd}"
    # for equal numerator and denominators
    problem = f"({a}/{b})/({c}/{d})"
    solution = x
    return problem, solution


divide_fractions = Generator("Fraction Division", 16, "(a/b)/(c/d)=", "x/y",
                             divideFractionsFunc)
